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
        print(f"[{datetime.now()}] Получение новостей об утечках...")
        news = self.perplexity.get_weekly_leaks_news()
        
        message = f"📰 Новости об утечках данных в РФ за неделю\n\n{news}\n\n#утечки #безопасность #данные"
        
        try:
            await self.bot.send_message(chat_id=self.channel_id, text=message)
            print(f"[{datetime.now()}] Новости успешно опубликованы")
        except TelegramError as e:
            print(f"[{datetime.now()}] Ошибка публикации: {e}")
    
    def schedule_posts(self):
        schedule.every().monday.at("10:00").do(lambda: asyncio.run(self.post_news()))
        schedule.every().thursday.at("10:00").do(lambda: asyncio.run(self.post_news()))
        
        print("Бот запущен. Расписание публикаций:")
        print("- Понедельник в 10:00")
        print("- Четверг в 10:00")
        
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    bot = LeakNewsBot()
    bot.schedule_posts()
