### API_FINAL_YATUBE:
## Описание проекта:

Yatube - социальная сеть для ведения блогов. В данном репозитории представлен CRUD проекта, привязанный к API для общения между серверами.

## Технологии:

Python, DjangoRestFramework, API

## Примеры запросов:
GET запросы:
    Получение публикаций - http://127.0.0.1:8000/api/v1/posts/
    Получение публикации - http://127.0.0.1:8000/api/v1/posts/{id}/
    Получение комментариев - http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
    Список сообществ - http://127.0.0.1:8000/api/v1/groups/
    Подписки - http://127.0.0.1:8000/api/v1/follow/

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Rebsun-web/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
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
## Информация об авторе:

Привет, меня зовут Никита. Я уже давно знаком с программированием, но только недавно начал серьезно этим заниматься.