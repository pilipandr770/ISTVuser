import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Завантаження моделі
model_path = 'random_forest_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Функція для передобробки даних
def preprocess_data(data):
    # Тут можна додати стандартні методи обробки, якщо потрібно
    # Наприклад, стандартизація числових змінних
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data

# Інтерфейс для користувача
st.title("Прогнозування Відтоку Клієнтів")

# Введення даних для нового клієнта
id = st.sidebar.number_input("ID клієнта", min_value=0, max_value=10000)  # Включення ID як ознаки
is_tv_subscriber = st.sidebar.selectbox("Підписка на ТВ-пакет", (0, 1))
is_movie_package_subscriber = st.sidebar.selectbox("Підписка на пакет фільмів", (0, 1))
subscription_age = st.sidebar.number_input("Вік підписки", min_value=0, max_value=100)
bill_avg = st.sidebar.number_input("Середній рахунок", min_value=0.0, max_value=500.0)
reamining_contract = st.sidebar.number_input("Залишок контракту", min_value=0.0, max_value=5.0)
service_failure_count = st.sidebar.number_input("Кількість збоїв", min_value=0, max_value=10)
download_avg = st.sidebar.number_input("Середня швидкість завантаження", min_value=0.0, max_value=100.0)
upload_avg = st.sidebar.number_input("Середня швидкість вивантаження", min_value=0.0, max_value=50.0)
download_over_limit = st.sidebar.selectbox("Завантаження перевищує ліміт", (0, 1))

# Створюємо DataFrame з введених даних, включаючи ID
input_data = pd.DataFrame({
    'id': [id],  # Додано 'id' як ознаку
    'is_tv_subscriber': [is_tv_subscriber],
    'is_movie_package_subscriber': [is_movie_package_subscriber],
    'subscription_age': [subscription_age],
    'bill_avg': [bill_avg],
    'reamining_contract': [reamining_contract],
    'service_failure_count': [service_failure_count],
    'download_avg': [download_avg],
    'upload_avg': [upload_avg],
    'download_over_limit': [download_over_limit]
})

# Передобробка даних, якщо це потрібно
processed_data = preprocess_data(input_data)

# Прогноз
prediction = model.predict(processed_data)

# Виведення результату
st.write("Ймовірність відтоку клієнта:", "Так" if prediction[0] == 1 else "Ні")
