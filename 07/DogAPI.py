import requests
import json

# URL API ресурсу
url = "https://dog.ceo/api/breeds/image/random"

# Параметри запиту (якщо потрібно)
params = {
    'param1': 'value1',
    'param2': 'value2'
}

# Виконання GET-запиту
response = requests.get(url, params=params)

# Перевірка статусу відповіді
if response.status_code == 200:
    # Конвертація в JSON
    data = response.json()
    
    # Виведення результату
    print(json.dumps(data, indent=4))
else:
    print(f"Error {response.status_code}: {response.text}")
