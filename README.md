#  Проект Kittygram

## Описание

Одностраничное приложение, в котором пользователи могут публиковать фото котиков, с информацией о них.

### База Данных

Для продакшен версии предполагается подключение БД PostgreSQL. Для этого нужно добавить в файл .env переменную окружения DB_POSTGRES = True и остальные переменные для Postgres согласно переменной DATABASES в settings.py.

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

### Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/BTARU/kittygram_final.git
```

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

## Технологии

Backend: Django Rest Framework, запущенный на web-сервере Gunicorn.

Frontend: React.

Связь между браузером пользователя и сервером настроена через Web-сервер Nginx.

## Автор

[Bulat Ayupov](https://github.com/BTARU)
