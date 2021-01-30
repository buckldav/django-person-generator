from django.db import models
from shutil import copy2
from datetime import datetime
import os

MEDIA_LOCATION = "persons"
class Person(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to=MEDIA_LOCATION, default=f"{MEDIA_LOCATION}/tmp.jpg")

  def save(self, *args, **kwargs):
    # Copy image to a new, unique file related to the person's name and the time of download
    new_filename = f"{self.name[:10]}-{datetime.now().isoformat()}"
    new_filename = "".join([c for c in new_filename if c.isalpha() or c.isdigit()]).rstrip() + ".jpg"
    copy2(f"media/{MEDIA_LOCATION}/tmp.jpg", f"media/{MEDIA_LOCATION}/{new_filename}")
    self.image = f"{MEDIA_LOCATION}/{new_filename}"
    super(Person, self).save(*args, **kwargs) 

  def delete(self, *args, **kwargs):
    # Delete the image file along with the model
    # The [1:] slice is to remove the / in front of /media/persons/...
    os.remove(self.image.url[1:])
    super(Person, self).delete(*args, **kwargs)

  def __str__(self):
    return f"Person {self.id}: {self.name}"