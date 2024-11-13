import logging
from typing import Any, Dict, List, Tuple

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

from db.crud import VocabCRUD, get_user_vocab_by_vocab_id, get_wordpairs_by_vocab_id
from db.database import Session
from db.models import Vocabulary
from src.filters.check_empty_filters import CheckEmptyFilter
from src.keyboards.vocab_base_kb import get_inline_kb_vocab_options, get_inline_kb_vocab_selection
from src.keyboards.vocab_trainer_kb import get_inline_kb_all_training
from text_data import MSG_ENTER_VOCAB, MSG_ERROR_VOCAB_BASE_EMPTY

router = Router(name='vocab_base')
logger: logging.Logger = logging.getLogger(__name__)


@router.callback_query(F.data == 'vocab_base')
async def process_vocab_base(callback: CallbackQuery) -> None:
    """Відстежує натискання на кнопку "База словників" у головному меню.
    Відправляє користувачу словники у вигляді кнопок.
    """
    user_id: int = callback.from_user.id
    check_empty_filter = CheckEmptyFilter()

    try:
        with Session() as session:
            vocab_crud = VocabCRUD(session=session, user_id=user_id)
            user_vocabs: list[Vocabulary] = vocab_crud.get_user_all_vocabs()
    except Exception as e:
        logger.error(e)
        return

    # Якщо в БД користувача немає словників
    if check_empty_filter.apply(user_vocabs):
        msg_text: str = MSG_ERROR_VOCAB_BASE_EMPTY
    else:
        msg_text: str = MSG_ENTER_VOCAB

    kb: InlineKeyboardMarkup = get_inline_kb_vocab_selection(vocabs=user_vocabs)
    await callback.message.edit_text(text=msg_text, reply_markup=kb)


@router.callback_query(F.data.startswith('select_vocab_'))
async def process_vocab_selection(callback: CallbackQuery, state: FSMContext) -> None:
    """Обробляє вибір словника"""
    data_fsm: Dict[str, Any] = await state.get_data()

    vocab_id = int(callback.data.split('select_vocab_')[1])
    await state.update_data(vocab_id=vocab_id)  # Додавання ID обраного словника

    with Session() as db:
        vocab_details: List[Dict] = get_wordpairs_by_vocab_id(db, vocab_id)
        user_vocab: dict = get_user_vocab_by_vocab_id(db, vocab_id)

    vocab_name: str = user_vocab.name
    vocab_note: str = user_vocab.description

    current_state: Any | None = data_fsm.get('current_state')  # Поточний стан FSM

    # Якщо був викликаний список словників з розділу бази словників
    if current_state == 'VocabBaseState':
        kb: InlineKeyboardMarkup = get_inline_kb_vocab_options()
        msg_finally: str = (
            f'Назва словника: {vocab_name}\n'
            f'Примітка: {vocab_note or 'Відсутня'}\n'
            f'Кількість словникових пар: {len(vocab_details)}\n\n'
            f'Словникові пари:\n')

        for idx, wordpairs_data in enumerate(vocab_details, start=1):
            words_lst: List[Tuple[str, str]] = wordpairs_data['words']
            translations_lst: List[Tuple[str, str]] = wordpairs_data['translations']
            annotation: str = wordpairs_data['annotation'] or 'Немає анотації'

            words_part: str = ', '.join([f'{word} [{transcription}]'
                                    if transcription else word
                                    for word, transcription in words_lst])
            translations_part: str = ', '.join([f'{translation} [{transcription}]'
                                        if transcription else translation
                                        for translation, transcription in translations_lst])

            msg_finally += f'{idx}. {words_part} : {translations_part} : {annotation}\n'
    # Якщо був викликаний список словників з розділу тренування
    elif current_state == 'VocabTrainState':
        msg_finally: str = f'Ви обрали словник: {vocab_name}\nОберіть, будь-ласка, тип тренування.'
        kb: InlineKeyboardMarkup = get_inline_kb_all_training()

    await callback.message.edit_text(text=msg_finally, reply_markup=kb)
