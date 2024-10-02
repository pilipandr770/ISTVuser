Прогнозування Відтоку Клієнтів Телекомунікаційної Компанії
Опис Проєкту
Цей проєкт присвячений розробці моделі машинного навчання для прогнозування відтоку клієнтів телекомунікаційної компанії. Мета полягає в ідентифікації клієнтів, які з високою ймовірністю можуть припинити користуватися послугами компанії, що дозволить вчасно вжити заходів для їх утримання.

Зміст
Опис Проєкту
Дані
Структура Проєкту
Вимоги
Установка
Використання
Результати
Аналіз Важливості Ознак
Контейнеризація з Docker
Автор
Дані
Набір даних містить інформацію про 72,274 клієнтів, включаючи:

Демографічні дані
Історію використання послуг
Тарифні плани
Інформацію про відток клієнтів
Файл даних: internet_service_churn.csv

Структура Проєкту
data/ — Папка з даними
internet_service_churn.csv — Сирі дані
processed_data.csv — Оброблені дані
models/ — Папка з збереженими моделями
random_forest_model.pkl — Збережена модель Random Forest
notebooks/ — Jupyter ноутбуки з кодом
churn_prediction.ipynb — Основний ноутбук з аналізом та моделлю
feature_importances.csv — Файл з важливістю ознак
README.md — Опис проєкту
Dockerfile — Файл для створення Docker образу
docker-compose.yml — Файл для Docker Compose
Вимоги
Python 3.7 або вище
Бібліотеки:
pandas
numpy
scikit-learn
matplotlib
seaborn
pickle
Установка
Клонування репозиторію:

bash
Копіювати код
git clone https://github.com/your_username/churn_prediction.git
cd churn_prediction
Створення віртуального середовища:

bash
Копіювати код
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
Встановлення залежностей:

bash
Копіювати код
pip install -r requirements.txt
Використання
Запуск ноутбука:

Використовуйте Jupyter Notebook або Jupyter Lab для відкриття файлу notebooks/churn_prediction.ipynb.

bash
Копіювати код
jupyter notebook notebooks/churn_prediction.ipynb
Виконання коду:

Послідовно виконуйте комірки ноутбука для:

Завантаження та обробки даних
Тренування моделі
Оцінки результатів
Збереження моделі та результатів
Результати
Точність моделі (Accuracy): 97.08%
Precision: 97.80%
Recall: 96.85%
F1 Score: 97.32%
Модель показує високі показники ефективності у прогнозуванні відтоку клієнтів.

Аналіз Важливості Ознак
Аналіз важливості ознак показав, що найбільший вплив на відтік клієнтів мають:

subscription_age — Вік підписки клієнта
bill_avg — Середній рахунок клієнта
reamining_contract — Залишок контракту
service_failure_count — Кількість збоїв у сервісі
Деталі знаходяться у файлі feature_importances.csv.

Контейнеризація з Docker
Для спрощення розгортання проєкту використовується Docker.

Створення Docker образу:

bash
Копіювати код
docker build -t churn_prediction_app .
Запуск контейнера:

bash
Копіювати код
docker run -p 8000:8000 churn_prediction_app
Docker Compose:

Для запуску з Docker Compose використовуйте:

bash
Копіювати код
docker-compose up
Автор
Ваше Ім'я — Data Scientist
