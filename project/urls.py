from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from project.persons.views import generate_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-image/', generate_image, name="generate-image")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
