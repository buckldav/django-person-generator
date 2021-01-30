## Project Setup
Create a Django project with a persons app.
```bash
pip install Django Pillow django-imagekit requests
django-admin startproject project .
cd project
django-admin startapp persons
```

Make sure to add `persons` to INSTALLED_APPS in `project/settings.py`.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'project.persons'
]
```

At the bottom of `settings.py` add media settings because we will be saving images.
```python
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
```

Create media directories in root of project.
```bash
media/
  persons/
project/ # our Django project
...
```

## Image Downloader
Create a view in `persons/views.py` that uses the requests library to download an image from
https://thispersondoesnotexist.com/image.
```python
from django.http import JsonResponse
from django.conf.global_settings import MEDIA_ROOT
import requests

def generate_image(request):
  # Use this site to generate an image file of a person
  url = 'https://thispersondoesnotexist.com/image'
  req = requests.get(url)
  # Adjust the names and paths below to fit your project
  filename = '/persons/tmp.png'
  file = open('media' + filename, 'wb+')
  # Write the file
  for chunk in req.iter_content(100000):
    file.write(chunk)
  file.close()

  return JsonResponse(data={
    "path": MEDIA_ROOT + filename
  })
```

Add the view to `urls.py` and the media static server.
```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from project.persons.views import generate_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-image/', generate_image)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Models and Admin
Create a Person model in `persons/models.py`. The `save()` method is overwritten to make sure that the image saved by default
(our generated image) gets saved as its own file.
```python
from django.db import models
from shutil import copy2
from datetime import datetime

class Person(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to="persons", default="persons/tmp.png")

  def save(self, *args, **kwargs):
    # Copy image to a new, unique file related to the person's name and the time of download
    location = "media/persons"
    new_filename = f"{self.name[:10]}-{datetime.now().isoformat()}"
    new_filename = "".join([c for c in new_filename if c.isalpha() or c.isdigit()]).rstrip() + ".png"
    copy2(f"{location}/tmp.png", f"{location}/{new_filename}")
    self.image = f"{location}/{new_filename}"
    super(Person, self).save(*args, **kwargs) 
```

Register the model in `persons/admin.py`.
```python
from django.contrib import admin
from project.persons.models import Person

admin.site.register(Person)
```

Be sure to migrate the database. I'm just using the default sqlite database from settings. Create a superuser too in order to log in to admin.
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

Once those things are set up, run the server and visit `127.0.0.1:8000/admin/` to try adding persons.