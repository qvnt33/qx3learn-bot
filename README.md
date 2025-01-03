# Lingoro Bot

![lingoro-bot](docs/images/icon.svg)
## Опис бота

**Lingoro Bot** — це Telegram-бот, який допомагає вивчати іноземні мови. Його основна ідея — створення персоналізованих словників для ефективного та цілеспрямованого навчання. Користувачі можуть додавати свої слова, переклади та анотації, адаптуючи бот під власні потреби.

## Команди

- `/start`, `/menu` — Запуск бота та відкриття головного меню.
- `/vocab_base` — Відображення всіх словників користувача.
- `/vocab_trainer` — Запуск тренажера для словникових пар.
- `/help` — Інструкції та приклади використання.

## Основна концепція

Бот побудований на ідеї **індивідуального навчання**, де користувач самостійно:
- Створює словники.
- Додає до них словникові пари (*слова, переклади та анотації*).

Це дозволяє зосередитись на тих словах, які для вас найважливіші.

## Можливості

- Створення персоналізованих словників.
- Тренування у форматах **Прямий переклад** та **Зворотній переклад**.
- Використання підказок та анотацій для ефективного навчання.
- Гнучка структура для додавання складних словникових пар із транскрипціями та поясненнями.

## Використання бота

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

## Як запустити бота

1. **Клонування репозиторію**:

    Завантажте проєкт на свій локальний компʼютер:
    ```bash
    git clone https://github.com/qvnt33/lingoro-bot.git
    cd lingoro-bot
    ```

3. **Встановлення залежностей**:

   Переконайтеся, що у вас встановлений **Python 3.9+** і менеджер пакетів **pip**. Для встановлення залежностей виконайте:
    ```bash
    pip install -r requirements.txt
    ```

4. **Налаштування оточення**:

   - Скопіюйте файл прикладу `.env.example` у `.env`:
        ```
        cp .env.example .env
        ```
    - Відредагуйте файл `.env` і додайте токен вашого бота:
       ```
        TOKEN=<your_bot_token>
        ```
        - **TOKEN**: Токен ви можете отримати у [BotFather](https://core.telegram.org/bots#botfather).

6. **Запуск бота**:

    Виконайте наступну команду з головної директорії проєкту:
    ```bash
    python -m lingoro_bot.bot
    ```

## Документація

- [Правила та валідація даних](docs/rules_and_validations.md)
- [Структура бази даних](docs/database_scheme.png)
- [Блок-схема роботи бота](docs/bot_flowchart.pdf)
