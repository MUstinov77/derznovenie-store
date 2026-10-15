# Дерзновение — сайт-визитка (Django)

## Разработка
    python3.14 -m venv .venv && .venv/bin/pip install -r requirements.txt
    cp .env.example .env     # для разработки поставьте DEBUG=True
    .venv/bin/python manage.py migrate
    .venv/bin/python manage.py createsuperuser
    .venv/bin/python manage.py runserver

Товары — в админке (`/admin/` или значение `ADMIN_URL`). Тексты секции «О бренде» — в `site_app/views.py`.

## Продакшен
1. Заполните `.env` (`DEBUG=False`, `SECRET_KEY`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, `TELEGRAM_URL`, `ADMIN_URL`).
2. `python manage.py migrate && python manage.py collectstatic --noinput`
3. Запуск: `gunicorn config.wsgi:application` (пример systemd — `deploy/gunicorn.service`).
4. nginx + HTTPS: `deploy/nginx.conf`; он же раздаёт `media/`. Статику отдаёт WhiteNoise.
5. Проверка: `python manage.py check --deploy`. Делайте бэкапы `db.sqlite3` и `media/`.

## Shared-хостинг (Reg.ru, ispmanager + Passenger)
Docker и GitHub Actions здесь не используются. Python 3.12+ включается в панели (Сайты → домен → Изменить → CGI-скрипты, Python).

    cd ~
    git clone https://github.com/MUstinov77/derznovenie-store.git derznovenie
    cd derznovenie
    /opt/python/ВЕРСИЯ/bin/python -m venv .venv
    .venv/bin/pip install -r requirements.txt
    mkdir -p data/media
    cp .env.example .env && nano .env      # см. ниже
    .venv/bin/python manage.py migrate
    .venv/bin/python manage.py collectstatic --noinput
    cp deploy/passenger_wsgi.py ~/www/ВАШ_ДОМЕН/passenger_wsgi.py   # и поправьте PROJECT_DIR
    ln -s ~/derznovenie/data/media ~/www/ВАШ_ДОМЕН/media            # раздача фото
    touch ~/www/ВАШ_ДОМЕН/.restart-app

В `.env`: `DEBUG=False`, `SECRET_KEY`, `ALLOWED_HOSTS=ваш-домен.ру,www.ваш-домен.ру`, `CSRF_TRUSTED_ORIGINS=https://...`,
`DATABASE_PATH=/полный/путь/derznovenie/data/db.sqlite3`, `MEDIA_ROOT=/полный/путь/derznovenie/data/media`,
`SECURE_SSL_REDIRECT=False` (включите после выпуска SSL-сертификата в панели).

Обновление: `cd ~/derznovenie && git pull && .venv/bin/pip install -r requirements.txt && .venv/bin/python manage.py migrate && .venv/bin/python manage.py collectstatic --noinput && touch ~/www/ВАШ_ДОМЕН/.restart-app`
