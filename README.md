# Агентство недвижимости

Это проект для управления объявлениями о недвижимости, который позволяет риелторам добавлять квартиры, фильтровать их по различным параметрам, включая новостройки, оставлять жалобы на объявления. Администраторы могут управлять квартирами, собственниками и жалобами через интерфейс админки.

## Установка:

- Python 3.x
- Django 3.x и выше
- PostgreSQL (или любая другая база данных, поддерживаемая Django)
- pip

### Установка зависимостей:

1. Клонируйте репозиторий:

```bash
   git clone https://github.com/AndreyBychenkow/Website-for-realtors
```

2. Установите зависимости:

```
pip install -r requirements.txt
```
3. Настройте файл settings.py в проекте Django, указав параметры подключения к вашей базе данных.

### Применение миграций и запуск сервера:

* После настройки базы данных выполните в терминале миграции:
```
python manage.py migrate
```
* Запустите сервер разработки в терминале:
```
python manage.py runserver
```
![запуск сервера](https://i.postimg.cc/nhfpbdX5/image.jpg)



## Использование:

- Перейдите по адресу  http://127.0.0.1:8000/ и вы попадете на сайт недвижимости, в котором вы можеет самостоятельно выбрать необходимые вам параметры поиска:

![сайт недвижимости](https://i.postimg.cc/WbVxzD9S/image.jpg)

- Используйте админку Django для управления данными сайта недвижимости. Для доступа к админке перейдите по адресу http://127.0.0.1:8000/admin/ и войдите с учетными данными суперпользователя.

- Здесь вы можете просмотреть множество нужной вам информации по недвижимости,а так же оставить жалобу или лайкнуть понравившуюся вам квартиру.

![инфа_1](https://i.postimg.cc/q7GNf6ZY/image.jpg)

![инфа_2](https://i.postimg.cc/T2spX6CR/image.jpg)

![жалоба](https://i.postimg.cc/0QB2xYGt/image.jpg)



## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
