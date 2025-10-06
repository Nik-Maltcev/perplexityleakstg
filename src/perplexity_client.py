import requests
from datetime import datetime, timedelta

class PerplexityClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.perplexity.ai/chat/completions"
    
    def get_weekly_leaks_news(self):
        today = datetime.now()
        week_ago = today - timedelta(days=7)
        
        prompt = f"""Создай качественный аналитический обзор инцидентов кибербезопасности за период с {week_ago.strftime('%d.%m.%Y')} по {today.strftime('%d.%m.%Y')}.

🌍 Регионы: Россия, Казахстан, Узбекистан, Таджикистан, Беларусь, Армения, Грузия

🎯 Типы инцидентов:
• Утечки персональных данных
• Взломы и хакерские атаки
• DDoS-атаки (особенно приведшие к утечкам)
• Компрометация систем с потенциальной утечкой данных
• Ransomware атаки с кражей данных

📊 Формат обзора:

1. 📈 ОБЩАЯ СТАТИСТИКА
   - Количество инцидентов по типам
   - Общий объём скомпрометированных данных
   - Тренды по сравнению с предыдущей неделей

2. 🔥 КРУПНЕЙШИЕ ИНЦИДЕНТЫ
   Для каждого инцидента:
   • 📅 Дата
   • 🏛️ Компания/организация
   • 🌎 Страна
   • 🎯 Тип атаки (утечка/взлом/DDoS/ransomware)
   • 📊 Масштаб (кол-во пострадавших/объём данных)
   • 📝 Тип данных (паспорта, карты, мед. данные и т.д.)
   • ⚠️ Метод атаки и уязвимость
   • 🛡️ Последствия и риски

3. 💡 АНАЛИТИКА И ВЫВОДЫ
   - Основные векторы атак
   - Наиболее подверженные сектора
   - Тренды в методах атак
   - Рекомендации по защите

❗ Требования:
- Только подтверждённые инциденты
- Конкретные цифры и факты
- Профессиональный тон
- Структурированность
- Фокус на инцидентах с утечками данных или их потенциалом

Если инцидентов не найдено, напиши: "🔒 За прошедшую неделю крупных инцидентов кибербезопасности в регионе не зафиксировано."""

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
            "max_tokens": 3000,
            "temperature": 0.3,
            "stream": False
        }
        
        try:
            response = requests.post(self.base_url, json=payload, headers=headers, timeout=60)
            response.raise_for_status()
            data = response.json()
            
            # Согласно документации, ответ в поле choices[0].message.content
            if 'choices' in data and len(data['choices']) > 0:
                return data['choices'][0]['message']['content']
            else:
                return "Не удалось получить ответ от API"
        except requests.exceptions.RequestException as e:
            return f"Ошибка при запросе к API: {str(e)}"
        except Exception as e:
            return f"Ошибка при обработке данных: {str(e)}"
