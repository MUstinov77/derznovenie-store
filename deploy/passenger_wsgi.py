# -*- coding: utf-8 -*-
"""
Точка входа для shared-хостинга (Passenger). Копируется в корень сайта
(например ~/www/ВАШ_ДОМЕН/passenger_wsgi.py). Сам проект лежит ВНЕ корня сайта,
чтобы .env, база и .git не были доступны из интернета.
"""
import glob
import os
import sys

# --- поправьте под свой хостинг (пути видны в панели и по команде `pwd`) ---
PROJECT_DIR = '/var/www/u3683474/data/site/derznovenie/derznovenie-store'
VENV_DIR = PROJECT_DIR + '/.venv'
# ---------------------------------------------------------------------------

sys.path.insert(0, PROJECT_DIR)
for site_packages in glob.glob(VENV_DIR + '/lib/python3.*/site-packages'):
    sys.path.insert(1, site_packages)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
