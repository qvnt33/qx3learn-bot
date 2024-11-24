# qx3learn-bot

![qx3learn-bot logo](docs/images/logo.png)

### Опис бота

**qx3learn-bot** — це Telegram-бот, який допомагає вивчати іноземні мови. Його основна ідея — створення персоналізованих словників для ефективного та цілеспрямованого навчання. Користувачі можуть додавати свої слова, переклади та анотації, адаптуючи бот під власні потреби.

### Основна концепція

Бот побудований на ідеї **індивідуального навчання**, де користувач самостійно:

- Створює словники.
- Додає до них словникові пари (слова, переклади та анотації).

Це дозволяє зосередитись на тих словах, які для вас найважливіші.

### Формат словникових пар

> word1 | word_transcription1, word2 | word_transcription2 : translation1 | translation_transcription1 : annotation
>
- **Частини** (*слова, переклади, анотація*):
    - **Слова:** word1 | word_transcription1, word2 | word_transcription2
    - **Переклади:** translation1 | translation_transcription1
    - **Анотація:** annotation
- **Елементи** (*слово або переклад із транскрипцією*):
    - **Основне слова з транскрипцією:** word1 | word_transcription1
    - **Основний переклад з транскрипцією:** translation1 | translation_transcription1
- **Компоненти** (*слово, переклад, транскрипція, анотація*):
    - **Основне слово:** word1 (*обовʼязково*)
    - **Транскрипція до word1:** word_transcription1 (*необовʼязково*)
    - **Основний переклад:** translation1 (*обовʼязково*)
    - **Транскрипція до translation1:** translation_transcription1 (*необовʼязково*)
    - **Анотація до словникової пари:** annotation (*необовʼязково*)

### Команди

- `/start`, `/menu` – Ініціалізує сесію користувача, перевіряє базу даних і відкриває головне меню.
- `/vocab_base` – Виводить список створених словників.
- `/vocab_trainer` – Переходить до розділу словникового тренажера.
- `/help` – Показує інструкції та приклади використання бота.

### Використання бота

1. **Створіть словник**:
    - Введіть назву.
    - Додайте примітку (*за бажанням*).
    - Додайте словникові пари у форматі, описаному вище.
2. **Обирайте тип тренування**:
    - Прямий переклад (*від слова до перекладу*).
    - Зворотній переклад (*від перекладу до слова*).
3. **Розпочинайте навчання**:
    - Бот надасть слово для перекладу, і ви зможете:
        - Відповісти.
        - Пропустити.
        - Дізнатися переклад.
        - Запросити анотацію або підказку.

### Як запустити бота

1. Клонування репозиторію:

```bash
git clone https://github.com/qvnt33/qx3learn-bot.git
```

1. Встановлення залежностей:

```bash
pip install -r requirements.txt
```

1. Налаштування оточення:

Створіть файл `.env` у кореневій директорії проєкту та додайте до нього наступні змінні:

```
TOKEN=<your_bot_token>
```

- TOKEN: Токен вашого бота, який ви отримаєте у [BotFather](https://core.telegram.org/bots#botfather).
1. Запуск бота:

```bash
python bot.py
```

## Документація

Додаткова інформація:

- Правила та валідація даних(docs/rules_and_validations.md)
- Схема бази даних(docs/database_scheme.png)
- Блок-схема роботи боту(docs/bot_flowchart.png)
