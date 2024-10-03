# Вибір базового образу Python
FROM python:3.9-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо всі файли до контейнера
COPY . /app

# Встановлюємо необхідні залежності
RUN pip install --no-cache-dir -r requirements.txt

# Відкриваємо порт 8501 для Streamlit
EXPOSE 8501

# Запускаємо Streamlit при старті контейнера
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
