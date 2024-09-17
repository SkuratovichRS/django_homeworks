## Инструкция
1. Создать `.env` с `SECRET_KEY`
2. Билд образа: `docker build -t crud:latest .`
3. Запуск контейнера: `docker run --env-file .env -p 8000:8000 -d crud:latest`
4. Проверка работы: http://localhost:8000/api/v1/
