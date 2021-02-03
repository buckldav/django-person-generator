from django.http import JsonResponse
from django.conf.global_settings import MEDIA_URL
import requests

def generate_image(request):
    # Use this site to generate an image file of a person
    url = 'https://thispersondoesnotexist.com/image'
    req = requests.get(url)
    # Adjust the names and paths below to fit your project
    filename = '/persons/tmp.jpg'
    # Write the file
    with open('media' + filename, 'wb+') as f:
        f.write(req.content)

    return JsonResponse(data={
        "path": MEDIA_URL + filename
    })