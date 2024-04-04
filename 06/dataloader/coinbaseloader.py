import requests
import pandas as pd

# Отримати список доступних продуктів
url = "https://api.pro.coinbase.com/products"
response = requests.get(url)
products = response.json()

# Перетворення в DataFrame
df_products = pd.DataFrame(products)
print(df_products)
# Вибрати 3 продукти
selected_products = df_products['id'].sample(3).tolist()

# Функція для отримання історичних даних
def get_historical_data(product_id, start_date, end_date, granularity):
    url = f"https://api.pro.coinbase.com/products/{product_id}/candles"
    params = {
        'start': start_date,
        'end': end_date,
        'granularity': granularity
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data, columns=['timestamp', 'low', 'high', 'open', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')  # Конвертація timestamp в datetime
    df.set_index('timestamp', inplace=True)  # Встановлення timestamp як індекс
    return df

# Отримання даних
start_date = '2022-01-01T00:00:00'
end_date = '2022-04-01T00:00:00'
granularity = 86400  # день

dfs = {}
for product in selected_products:
    dfs[product] = get_historical_data(product, start_date, end_date, granularity)

# Виведення DataFrame
for product, df in dfs.items():
    print(f"\n{product}:\n{df.head()}")
