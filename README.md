# books-rest-api

Пример реализации Rest Api

## Установка и запуск

1. Клонировать репозиторий с Github.com:
````
git clone https://github.com/Povarenskiy/books-rest-api.git
cd books-rest-api
````
2. Запуск docker-compose
````
docker-compose up -d
````
3. Создание администратора
````
docker-compose run web python manage.py createsuperuser
````

## Панель администратора
````
http://localhost:8000/admin/
````

## Api

````http://localhost:8000/api/v1/```` - api проекта

````http://localhost:8000/api/v1/books/```` - список книги

````http://localhost:8000/api/v1/books/<pk>/```` - детальная информация по книге  

````http://localhost:8000/api/v1/chapters/<pk>/```` - детальная информация по главе  

````http://localhost:8000/api/v1/chapters/<pk>/like/```` - эндпоинт для поставки лайка к главе (Chapter)


