# Telegram Leak News Bot

Телеграм бот для автоматической публикации новостей об утечках данных в РФ.

## Переменные окружения

### Обязательные

```bash
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHANNEL_ID=@your_channel_name
PERPLEXITY_API_KEY=your_perplexity_api_key_here
```

### Опциональные

```bash
POST_TIME_MONDAY=10:00
POST_TIME_THURSDAY=10:00
TIMEZONE=Europe/Moscow
```

## Локальная установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Создайте файл `.env`:
```bash
cp .env.example .env
```

3. Заполните переменные окружения в `.env`

4. Запустите бота:
```bash
cd src
python bot.py
```

## Развертывание на Railway

Подробная инструкция в файле [DEPLOYMENT.md](DEPLOYMENT.md)

### Быстрый старт:

1. Загрузите код на GitHub
2. Создайте проект на [railway.app](https://railway.app)
3. Подключите GitHub репозиторий
4. Добавьте переменные окружения в Railway
5. Деплой произойдет автоматически

## Получение токенов

### Telegram Bot Token
1. Напишите [@BotFather](https://t.me/BotFather)
2. Команда `/newbot`
3. Скопируйте токен
4. Добавьте бота в канал как администратора

### Perplexity API Key
1. Зайдите на [perplexity.ai/settings/api](https://www.perplexity.ai/settings/api)
2. Создайте API ключ
3. Скопируйте ключ

### Telegram Channel ID
- Используйте `@username` канала, или
- Получите числовой ID через [@userinfobot](https://t.me/userinfobot)

## Расписание публикаций

По умолчанию:
- Понедельник в 10:00 (МСК)
- Четверг в 10:00 (МСК)

Изменить можно через переменные окружения `POST_TIME_MONDAY` и `POST_TIME_THURSDAY`
