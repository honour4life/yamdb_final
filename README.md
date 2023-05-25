![GitHubActionS](https://github.com/honour4life/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# api_yamdb
API к платформе для оставления отзывов к произведениям, составления рейтингов и комментирования отзывов

## Требования
- Python (3.7+)

### Пакеты:
- Django (3.2)
- djangorestframework (3.12.4)
- djangorestframework-simplejwt (4.7.2)

## Установка
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:honour4life/yamdb_final.git
cd yamdb_final/infra
```

Создание файла .env в директории infra:
```bash
touch .env 
```

Заполнить файл .env по следующему образцу:
```
SECRET_KEY=...# введите ваш секретный ключ!
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

Установите приложение docker, запустите и выполните следующие команды:
```bash
docker-compose up -d # сборка контейнеров
```

Выполнить миграции:
```bash
docker-compose exec web python manage.py migrate
```

Создаем superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```
Собираем статику:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

Фикстуры загружаемся следующей командой:
```bash
docker-compose exec web python manage.py csvfullfillment
```

## Автор
- [Марсель](https://github.com/honour4life)

## Ссылка на проект
- http://158.160.69.93/redoc/

