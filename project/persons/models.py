from django.db import models
from shutil import copy2
from datetime import datetime
import os
from PIL import Image  

MEDIA_LOCATION = "persons"
DEFAULT = "tmp.jpg"
class Person(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to=MEDIA_LOCATION, default=f"{MEDIA_LOCATION}/{DEFAULT}")

  def save(self, *args, **kwargs):
    if DEFAULT in self.image.url:
      # Copy image to a new, unique file related to the person's name and the time of download
      new_filename = f"{self.name[:10]}-{datetime.now().isoformat()}"
      new_filename = "".join([c for c in new_filename if c.isalpha() or c.isdigit()]).rstrip() + ".jpg"
      copy2(f"media/{MEDIA_LOCATION}/{DEFAULT}", f"media/{MEDIA_LOCATION}/{new_filename}")
      self.image = f"{MEDIA_LOCATION}/{new_filename}"
    # Save the image and resize it
    super(Person, self).save(*args, **kwargs) 
    # The [1:] slice is to remove the / in front of /media/persons/...
    im = Image.open(self.image.url[1:])  
    if im.width > 150: 
      im = im.resize((150, 150))
    im.save(self.image.url[1:])

  def delete(self, *args, **kwargs):
    # Delete the image file along with the model
    try:
      os.remove(self.image.url[1:])
    except:
      pass
    super(Person, self).delete(*args, **kwargs)

  def __str__(self):
    return f"Person {self.id}: {self.name}"