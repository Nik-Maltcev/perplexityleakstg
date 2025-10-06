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

🎯 Фокус на:
• Крупные утечки персональных данных
• Атаки на известные компании
• Взломы и хакерские атаки
• DDoS-атаки с последствиями
• Ransomware атаки
• Инциденты с финансовыми последствиями

📊 Формат ответа - структурированный обзор:

1. 📈 ОБЩАЯ СТАТИСТИКА
   - Количество значимых инцидентов за неделю
   - Общий масштаб (пострадавших/данных)

2. 🔥 КРУПНЕЙШИЕ ИНЦИДЕНТЫ (минимум 1, максимум 5-7)
   Для каждого:
   • 📅 Дата
   • 🏛️ Компания/организация
   • 🌎 Страна
   • 🎯 Тип атаки
   • 📊 Масштаб
   • 📝 Тип данных
   • ⚠️ Метод атаки
   • 🛡️ Последствия
   • 🔗 Источник информации

3. 💡 ВЫВОДЫ
   - Основные тренды
   - Рекомендации

❗ Требования:
- ТОЛЬКО свежие новости за указанный период
- ТОЛЬКО подтверждённые инциденты из надёжных источников
- Конкретные цифры и факты
- Если за неделю нет значимых инцидентов - напиши об этом честно

Если инцидентов не найдено: "🔒 За прошедшую неделю крупных инцидентов кибербезопасности в регионе не зафиксировано.\""""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "sonar-pro",
            "messages": [
                {"role": "system", "content": "Ты - эксперт-аналитик по кибербезопасности, специализирующийся на утечках данных, взломах и DDoS-атаках. Создавай профессиональные, структурированные обзоры с конкретными цифрами, фактами и техническими деталями атак."},
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
