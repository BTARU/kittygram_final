# Backend часть приложения Kittygram

#### База Данных

Для продакшен версии предполагается подключение БД PostgreSQL. Для этого нужно добавить переменную окружения DB_POSTGRES = True и остальные переменные для Postgres согласно переменной DATABASES в settings.py.

### Как запустить проект(продакшен):

Проект запускается в трех контейнерах Docker, связанных между собой Docker Network.

Для запуска проекта на сервере Ubuntu в контейнерах docker выполните команды в терминале:

```
sudo docker compose -f docker-compose.production.yml up -d
```

Сбор статики и выполнений миграций БД.

```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
```

```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
```

```
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```

### Как запустить только backend часть проекта локально:

Нужно изменить БД с Postgres на SQLite. Для этого удалите переменную DB_POSTGRES в файле окружения .env

Выполняем команды в терминале:

```
cd backend
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```