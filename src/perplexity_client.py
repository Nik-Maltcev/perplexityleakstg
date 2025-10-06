import requests
from datetime import datetime, timedelta

class PerplexityClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.perplexity.ai/chat/completions"
    
    def get_weekly_leaks_news(self):
        today = datetime.now()
        week_ago = today - timedelta(days=7)
        
        prompt = f"""Найди самые значимые новости об утечках данных и кибербезопасности за период с {week_ago.strftime('%d.%m.%Y')} по {today.strftime('%d.%m.%Y')}.

🌍 Регионы: Россия, Казахстан, Узбекистан, Таджикистан, Беларусь, Армения, Грузия

🎯 Фокус: крупные утечки, атаки на известные компании, взломы, DDoS, ransomware, финансовые инциденты

📊 ФОРМАТ ОТВЕТА (БЕЗ MARKDOWN!):

📈 СТАТИСТИКА
Количество инцидентов: X
Пострадавших: Y

🔥 ИНЦИДЕНТЫ (1-5 самых значимых):

▪️ ИНЦИДЕНТ 1
📅 Дата: ДД.ММ.ГГГГ
🏛 Компания: Название
🌎 Страна: Страна
🎯 Тип: утечка/взлом/DDoS/ransomware
📊 Масштаб: конкретные цифры
📝 Данные: тип данных
⚠️ Метод: как произошло
🛡 Последствия: что случилось

▪️ ИНЦИДЕНТ 2
...

💡 ВЫВОДЫ
• Тренд 1
• Тренд 2
• Рекомендация

❗ ВАЖНО:
- Используй ТОЛЬКО эмодзи, пробелы и переносы строк
- НЕ используй markdown (**, __, ##, -, *)
- Используй ▪️ для пунктов списка
- Используй • для подпунктов
- ТОЛЬКО свежие новости за период
- ТОЛЬКО проверенные источники
- Если нет инцидентов: "🔒 За неделю крупных инцидентов не зафиксировано.\""""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "sonar-pro",
            "messages": [
                {"role": "system", "content": "Ты - эксперт по кибербезопасности. Создавай обзоры БЕЗ markdown форматирования. Используй ТОЛЬКО эмодзи, пробелы, переносы строк и символы ▪️ и •. НЕ используй **, __, ##, -, * для форматирования."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 2500,
            "temperature": 0.3,
            "stream": False
        }
        
        try:
            response = requests.post(self.base_url, json=payload, headers=headers, timeout=60)
            response.raise_for_status()
            data = response.json()
            
            if 'choices' in data and len(data['choices']) > 0:
                return data['choices'][0]['message']['content']
            else:
                return "Не удалось получить ответ от API"
        except requests.exceptions.RequestException as e:
            return f"Ошибка при запросе к API: {str(e)}"
        except Exception as e:
            return f"Ошибка при обработке данных: {str(e)}"
