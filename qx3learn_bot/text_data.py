# handlers/create_vocab.py
MSG_ENTER_VOCAB_NAME = 'Введіть назву словника:'
MSG_ENTER_NEW_VOCAB_NAME = 'Введіть нову назву словника або натисніть "Залишити поточну назву".'
MSG_ENTER_VOCAB_DESCRIPTION = 'Введіть опис словника або натисніть "Пропустити", якщо опис не потрібен.'
MSG_ENTER_WORDPAIRS = (
    '📝 Введіть "словникові пари" у форматі:\n'
    'w1 | tr1 , w2 | tr2 : t1, t2 : a\n\n'
    '- w — слово\n'
    '- tr — транскрипція (опціонально).\n'
    '- t — переклад.\n'
    '- a — анотація (опціонально).\n\n'
    '📌 Примітки:\n'
    '*Слово, переклад, анотація розділяються символом ":"\n'
    '*Слово та транскрипція розділяються символом "|"\n'
    '*Можна додати декілька слів чи перекладів, розділяючи їх символом "," (опціонально)\n\n'
    '(В одному повідомленні можна ввести декілька словникових пар, кожну у новому рядку)')
MSG_ENTER_WORDPAIRS_SMALL_INSTRUCTIONS = ('📝 Введіть словникові пари у форматі:\n'
                                          'w1 | tr1 , w2 | tr2 : t1, t2 : a\n')
MSG_ERROR_VOCAB_NAME_DUPLICATE = ('⚠️ Нова назва словника не може збігатися з поточною.\n\n'
                                  'Введіть нову назву або натисніть "Залишити поточну назву".')
MSG_ERROR_VOCAB_NAME_INVALID = ('⚠️ У назві словника "{name}" знайдено помилки:\n'
                                '{errors}')
MSG_ERROR_VOCAB_DESCRIPTION_INVALID = ('⚠️ У примітці "{description}" до словника "{name}" знайдено помилки:\n'
                                       '{errors}')
MSG_ERROR_WORDPAIRS_NO_VALID = '⚠️ Немає жодної валідної словникової пари.'
MSG_ERROR_NO_VALID_WORDPAIRS_ADDED = '❌ Не вдалося зберегти словник, оскільки немає валідних словникових пар.'
MSG_SUCCESS_VOCAB_SAVED_TO_DB = '✅ Словник "{name}" успішно збережено до бази словників!'
MSG_SUCCESS_ALL_WORDPAIRS_VALID = '🎉 Усі введені словникові пари валідні!'
MSG_INFO_ADDED_WORDPAIRS = ('✅ Додано словникові пари:\n'
                            '{wordpairs}')
MSG_INFO_NO_ADDED_WORDPAIRS = ('❌ Не додано словникові пари:\n'
                               '{wordpairs}')
MSG_CONFIRM_CANCEL_CREATE_VOCAB = '❓ Ви дійсно хочете скасувати створення словника?'


# handlers/menu.py
MSG_TITLE_MENU = '🏠 Головне меню'
MSG_TITLE_MENU_FOR_NEW_USER = ('👋 Привіт! Ласкаво просимо до бота для вивчення слів!\n\n'
                               '🏠 Головне меню')


# handlers/vocab_base.py
MSG_CHOOSE_VOCAB = ('📗 Оберіть словник із вашої бази для перегляду або редагування.\n'
                    '➕ Щоб створити новий словник, натисніть кнопку “Додати словник”.')
MSG_INFO_VOCAB_BASE_EMPTY = ('❗️ У вашій базі поки що немає словників.\n\n'
                              'Для створення словників, натисніть на кнопку "Додати словник".')
MSG_CONFIRM_DELETE_VOCAB = '❓ Ви дійсно хочете видалити словник "{name}"?'
MSG_SUCCESS_VOCAB_DELETED = '✅ Словник "{name}" успішно видалено з бази словників.'


# handlers/vocab_trainer.py
MSG_INFO_VOCAB_BASE_EMPTY_FOR_TRAINING = ('❗️ У вашій базі поки що немає словників.\n\n'
                                          'Створіть новий словник у розділі "База словників", щоб почати тренування.')
MSG_CHOOSE_VOCAB_FOR_TRAINING = '📗 Оберіть словник із вашої бази для початку тренування.'
MSG_CHOOSE_TRAINING_MODE = ('📗 Словник: {name}\n\n'
                            '🎯 Оберіть тип тренування, щоб продовжити.')
MSG_CONFIRM_CANCEL_TRAINING = ('❓ Ви дійсно хочете завершити тренування?\n'
                               'Усі результати будуть збережені.')
MSG_CORRECT_ANSWER = ('✅ Вірно!\n'
                      '{words} -> {translations}')
MSG_WRONG_ANSWER = ('❌ Неправильно!\n'
                    '"{words}" не перекладається як "{user_translation}"')
MSG_LEFT_ONE_WORD_TRAINING = '⚠️ Залишилось останнє слово. Пропускати більше не можна!'
MSG_SHOW_WORDPAIR_ANNOTATION = ('💡 Показ анотації\n\n'
                                '📝 Слово(а): {words}\n'
                                '📝 Анотація: {annotation}')
MSG_SHOW_WORDPAIR_TRANSLATION = ('💬 Показ перекладу\n\n'
                                 '📝 Слово(а): {words}\n'
                                 '📝 Переклад(и): {translations}\n'
                                 '📝 Анотація: {annotation}')


# handlers/help.py
MSG_TITLE_HELP = """
📚 Допомога: Як користуватися ботом для вивчення слів

---

1️⃣ Як додати новий словник

Кроки для створення словника:
1. Додати назву словника:
  - Введіть назву словника в повідомленні.
    - Вимоги до назви: Унікальна для вашого облікового запису, без спеціальних символів.

2. Додати примітку (опціонально):
    - Примітка може бути корисною для опису теми словника чи контексту.
    - Якщо примітка не потрібна, натисніть кнопку "Пропустити".

3. Додати словникові пари:
    - Після створення словника додайте слова та їх переклади у форматі:
        слово | транскрипція, : переклад, переклад2 : анотація

    Приклади:
    - cat | kæt : кіт
    - dog : пес
    - book | bʊk : книга, підручник : об'єкт для читання
    - sun : сонце : небесне тіло

    Опис полів:
    - Слово (обов’язкове): Те, що ви вивчаєте.
    - Транскрипція (опціонально): Написання слова у фонетичному форматі після "|".
    - Переклад (обов’язкове): Переклади через ":".
    - Анотація (опціонально): Додатковий опис або контекст.

---

2️⃣ Типи тренувань

Після створення словника можна обрати один із двох типів тренувань:

✅ Прямий переклад (W -> T):
    - Ви бачите слово (або кілька слів), і потрібно ввести їх переклад.
    - Мета: Перевірити, як добре ви пам’ятаєте переклади.

📝 Зворотний переклад (T -> W):
    - Ви бачите переклад, і потрібно ввести відповідне слово.
    - Мета: Перевірити, наскільки добре ви пам’ятаєте написання слів іноземною мовою.

---

3️⃣ Додаткові можливості

- Перегляд бази словників:
  Ви можете переглядати всі створені словники та словникові пари в меню бази словників.

- Редагування та видалення:
  Ви можете редагувати або видаляти словникові пари в будь-який момент.

---

4️⃣ Ключові повідомлення

- Попередження:
  Якщо у словнику є помилки, бот повідомить вас і дозволить їх виправити.

- Збереження:
  Бот повідомить про успішне збереження словника або пари.

---

Цей бот допоможе вам:
- Легко додавати нові слова для вивчення.
- Тренувати переклад і написання.
- Підтримувати словниковий запас у порядку.

📖 Залишайтеся в ритмі вивчення мов і досягайте своїх цілей! 💪
"""


# validators/vocab/vocab_name_validator.py
MSG_ERROR_VOCAB_NAME_UNIQUELY = 'У вашій базі вже є словник з назвою "{name}". Введіть іншу назву.'
MSG_ERROR_VOCAB_NAME_INVALID_LENGTH = 'Довжина назви словника має бути від {min_length} до {max_length} символів.'
MSG_ERROR_VOCAB_NAME_INVALID_CHARS = 'Назва словника може містити лише літери, цифри та символи: "{allowed_chars}".'


# validators/vocab/vocab_description_validator.py
MSG_ERROR_VOCAB_DESCRIPTION_INVALID_LENGTH = ('Довжина опису словника має бути від '
                                              '{min_length} до {max_length} символів.')


# validators/wordpair/wordpair_validator.py
MSG_ERROR_WORDPAIR_MIN_REQUIREMENT = ('Словникова пара повинна містити хоча б одне слово та один переклад, '
                                      'розділені символом "{separator}".')
MSG_ERROR_WORDPAIR_MAX_REQUIREMENT = 'Словникова пара може містити максимум три частини: слово, переклад і анотацію.'


# validators/wordpair/component_validator.py
MSG_ERROR_COMPONENT_INVALID_LENGTH = ('Довжина компонента "{component}" має бути від '
                                      '{min_length} до {max_length} символів.')
MSG_ERROR_COMPONENT_INVALID_CHARS = ('Компонент "{component}" може містити лише '
                                     'літери, цифри та символи: "{allowed_chars}".')
