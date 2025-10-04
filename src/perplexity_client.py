import requests
from datetime import datetime, timedelta

class PerplexityClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.perplexity.ai/chat/completions"
    
    def get_weekly_leaks_news(self):
        today = datetime.now()
        week_ago = today - timedelta(days=7)
        
        prompt = f"""Найди последние новости об утечках персональных данных в России за период с {week_ago.strftime('%d.%m.%Y')} по {today.strftime('%d.%m.%Y')}.

Требования:
- Только утечки данных в РФ
- Только за указанный период
- Укажи дату, компанию/организацию, масштаб утечки
- Формат: краткая сводка для каждой утечки

Если утечек не найдено, напиши об этом."""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "sonar-pro",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 2000,
            "temperature": 0.2,
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
