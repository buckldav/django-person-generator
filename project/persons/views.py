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