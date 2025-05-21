#!/bin/sh

# Создаем директорию для миграций, если ее нет
if [ ! -d "migrations" ]; then
    echo "Initializing migrations directory..."
    flask db init
fi

# Проверяем, есть ли миграции
if [ ! "$(ls -A migrations/versions 2>/dev/null)" ]; then
    echo "Creating initial migration..."
    flask db migrate -m "initial migration"
fi

# Применяем миграции
echo "Running database migrations..."
flask db upgrade

# Запускаем приложение
echo "Starting application..."
exec "$@" 