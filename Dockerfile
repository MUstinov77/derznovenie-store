FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DATABASE_PATH=/data/db.sqlite3 \
    MEDIA_ROOT=/data/media

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# статика собирается на этапе сборки; значения нужны только чтобы settings импортировались
RUN SECRET_KEY=build-only ALLOWED_HOSTS=build python manage.py collectstatic --noinput

RUN useradd --system --no-create-home app && mkdir -p /data/media && chown -R app /data
USER app
VOLUME /data

EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate --noinput && exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3"]
