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
