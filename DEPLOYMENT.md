# Развертывание на Railway

## Переменные окружения для Railway

Добавьте следующие переменные в настройках Railway:

### Обязательные переменные

```bash
# Telegram Bot Token (получить у @BotFather)
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# Telegram Channel ID (например: @your_channel или -1001234567890)
TELEGRAM_CHANNEL_ID=@your_channel_name

# Perplexity API Key (получить на https://www.perplexity.ai/settings/api)
PERPLEXITY_API_KEY=your_perplexity_api_key_here
```

### Опциональные переменные

```bash
# Время публикации (по умолчанию 10:00)
POST_TIME_MONDAY=10:00
POST_TIME_THURSDAY=10:00

# Часовой пояс (по умолчанию Europe/Moscow)
TIMEZONE=Europe/Moscow
```

## Инструкция по развертыванию

### 1. Подготовка репозитория

```bash
# Создайте репозиторий на GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/telegram-leak-bot.git
git push -u origin main
```

### 2. Настройка Railway

1. Зайдите на [railway.app](https://railway.app)
2. Нажмите "New Project" → "Deploy from GitHub repo"
3. Выберите ваш репозиторий
4. Railway автоматически определит Python проект

### 3. Добавление переменных окружения

1. Откройте проект в Railway
2. Перейдите в раздел "Variables"
3. Добавьте все переменные из списка выше
4. Нажмите "Deploy"

### 4. Настройка Telegram бота

#### Получение Bot Token:
1. Напишите [@BotFather](https://t.me/BotFather) в Telegram
2. Отправьте команду `/newbot`
3. Следуйте инструкциям
4. Скопируйте полученный токен

#### Получение Channel ID:
1. Создайте канал в Telegram
2. Добавьте бота в канал как администратора
3. Используйте `@username` канала или числовой ID

Для получения числового ID:
- Отправьте сообщение в канал
- Перешлите его боту [@userinfobot](https://t.me/userinfobot)
- Скопируйте ID канала (начинается с `-100`)

### 5. Получение Perplexity API Key

1. Зайдите на [perplexity.ai](https://www.perplexity.ai/settings/api)
2. Войдите в аккаунт
3. Перейдите в Settings → API
4. Создайте новый API ключ
5. Скопируйте ключ

### 6. Проверка работы

После деплоя проверьте логи в Railway:
- Должно появиться сообщение "Бот запущен. Расписание публикаций:"
- Проверьте, что расписание настроено правильно

## Структура проекта для Railway

```
telegram_leak_bot/
├── src/
│   ├── perplexity_client.py  # Клиент Perplexity API
│   └── bot.py                # Основной бот
├── requirements.txt          # Зависимости Python
├── runtime.txt              # Версия Python (опционально)
└── Procfile                 # Команда запуска (опционально)
```

## Procfile (опционально)

Создайте файл `Procfile` в корне проекта:

```
worker: cd src && python bot.py
```

## runtime.txt (опционально)

Создайте файл `runtime.txt` для указания версии Python:

```
python-3.11.0
```

## Мониторинг

Railway предоставляет:
- Логи в реальном времени
- Метрики использования ресурсов
- Автоматический перезапуск при сбоях

## Стоимость

Railway предоставляет:
- $5 бесплатных кредитов в месяц
- Оплата по факту использования
- Примерная стоимость: $5-10/месяц для небольшого бота

## Альтернативные платформы

Если Railway не подходит, можно использовать:
- **Heroku** (платный)
- **Render** (бесплатный tier)
- **Fly.io** (бесплатный tier)
- **PythonAnywhere** (бесплатный tier с ограничениями)

## Troubleshooting

### Бот не запускается
- Проверьте логи в Railway
- Убедитесь, что все переменные окружения установлены
- Проверьте правильность токенов

### Бот не публикует сообщения
- Убедитесь, что бот добавлен в канал как администратор
- Проверьте правильность TELEGRAM_CHANNEL_ID
- Проверьте логи на наличие ошибок

### Ошибки Perplexity API
- Проверьте баланс API ключа
- Убедитесь, что ключ активен
- Проверьте лимиты запросов

## Поддержка

При возникновении проблем:
1. Проверьте логи в Railway
2. Убедитесь в правильности всех переменных
3. Проверьте документацию Perplexity API
