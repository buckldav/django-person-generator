# django-person-generator
Django person models with auto-generated pictures using thispersondoesnotexist.com.

## Setup
```bash
# Create and activate virtual env
python3 -m venv env
source env/bin/activate
# Install requirements
pip install -r requirements.txt
# Create SECRET_KEY
python3 -c "import secrets; print(f'SECRET_KEY={secrets.token_urlsafe()}')" > .env
# Migrate sqlite db and run server
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Tutorial
Visit [https://dev.to/buckldav/django-person-image-generator-29c8](https://dev.to/buckldav/django-person-image-generator-29c8) for a walkthrough on how to build this.