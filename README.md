    project/
    ├── .gitignore                  # Игнорируемые файлы
    ├── docker-compose.yml          # Оркестрация контейнеров
    ├── .env                        # Секреты (SECRET_KEY, DB_CREDS)
    ├── init-db.sh                  # Скрипт инициализации БД
    ├── nginx/
    │   └── nginx.conf              # Прокси /dash/ → dash_app
    └── services/
        ├── backend/                # Django-приложение
        │   ├── Dockerfile
        │   ├── requirements.txt    # Django, gunicorn, psycopg2, djangorestframework
        │   ├── gunicorn.conf.py
        │   └── src/
        │       ├── manage.py
        │       ├── config/
        │       │   ├── settings.py # API_ENDPOINT = "http://dash_app:8050"
        │       │   └── urls.py
        │       ├── core/
        │       │   ├── models.py   # User, Test, Question, Result
        │       │   ├── views.py    # Главная, тест, авторизация
        │       │   ├── urls.py
        │       │   └── templates/
        │       │       └── dashboard.html  # <iframe src="{{ DASH_URL }}">
        │       └── api/
        │           └── views.py    # API для данных статистики
        │
        └── dash_app/               # Микросервис Dash
            ├── Dockerfile
            ├── requirements.txt    # dash, pandas, plotly, gunicorn
            └── src/
                ├── app.py          # Код дашборда
                └── callbacks.py    # Логика обновления графиков
