from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EXAMPLE_PG_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'docudb',
        'USER': 'postgres',
        'PASSWORD': 'copybook',
        'HOST': 'localhost',
        'PORT': '5433', 
    }
}