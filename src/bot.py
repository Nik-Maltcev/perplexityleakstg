import os
import asyncio
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv
from telegram import Bot
from telegram.error import TelegramError
from perplexity_client import PerplexityClient

load_dotenv()

class LeakNewsBot:
    def __init__(self):
        self.bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
        self.channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
        self.perplexity = PerplexityClient(os.getenv('PERPLEXITY_API_KEY'))
    
    async def post_news(self):
        print(f"[{datetime.now()}] Начало публикации...")
        print(f"[{datetime.now()}] Channel ID: {self.channel_id}")
        
        try:
            print(f"[{datetime.now()}] Запрос к Perplexity API...")
            news = self.perplexity.get_weekly_leaks_news()
            print(f"[{datetime.now()}] Получен ответ: {news[:100]}...")
            
            message = f"📰 Новости об утечках данных в РФ за неделю\n\n{news}\n\n#утечки #безопасность #данные"
            
            print(f"[{datetime.now()}] Отправка в Telegram...")
            await self.bot.send_message(chat_id=self.channel_id, text=message)
            print(f"[{datetime.now()}] ✅ Успешно опубликовано")
        except TelegramError as e:
            print(f"[{datetime.now()}] ❌ Ошибка Telegram: {e}")
        except Exception as e:
            print(f"[{datetime.now()}] ❌ Общая ошибка: {e}")
    
    def schedule_posts(self):
        schedule.every().monday.at("10:00").do(lambda: asyncio.run(self.post_news()))
        schedule.every().thursday.at("10:00").do(lambda: asyncio.run(self.post_news()))
        
        print("="*50)
        print("🤖 Бот запущен успешно!")
        print(f"📢 Channel ID: {self.channel_id}")
        print(f"📅 Расписание публикаций:")
        print("   - Понедельник в 10:00 (МСК)")
        print("   - Четверг в 10:00 (МСК)")
        print(f"⏰ Текущее время: {datetime.now()}")
        print("="*50)
        
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    import sys
    
    try:
        bot = LeakNewsBot()
        
        # Тестовая публикация при запуске с аргументом --test
        if len(sys.argv) > 1 and sys.argv[1] == "--test":
            print("🧪 ТЕСТОВЫЙ РЕЖИМ: Публикация сейчас...")
            asyncio.run(bot.post_news())
            print("✅ Тест завершён")
        else:
            bot.schedule_posts()
    except Exception as e:
        print(f"❌ Критическая ошибка при запуске: {e}")
        raise
