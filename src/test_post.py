import asyncio
from bot import LeakNewsBot

async def test():
    bot = LeakNewsBot()
    await bot.post_news()

if __name__ == "__main__":
    asyncio.run(test())
