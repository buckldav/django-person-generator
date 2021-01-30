from django.contrib import admin
from django.db import models
from django.forms.widgets import ClearableFileInput # This is what ImageFields use by default, we're going to customize ours a little.

from project.persons.models import Person

class ImageWidget(ClearableFileInput):
  template_name = "image_widget.html"

class PersonAdmin(admin.ModelAdmin):
  formfield_overrides = {
    models.ImageField: {'widget': ImageWidget},
  }

admin.site.register(Person, PersonAdmin)
