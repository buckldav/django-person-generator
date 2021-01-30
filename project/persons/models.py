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