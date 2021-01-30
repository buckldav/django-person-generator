# imagekit-example
Django person models with auto-generated pictures using django-imagekit and thispersondoesnotexist.com.

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