from django.http import HttpResponse
from django.shortcuts import render
from imgtest import models
import base64
# Create your views here.


def saveImage(request):
    if request.method == "POST":
        file = request.FILES
        imgtmp = file.get('image', None).read()
        temp = models.ImageModel()
        temp.filename = 'WeChat_img'
        temp.data.put(imgtmp, content_type='image/jpeg')
        temp.save()
        return HttpResponse("---Success---")


def viewImage(request):
    image = models.ImageModel.objects(filename='WeChat_img').first()
    temp_data = image.data.read()
    temp_data = base64.b64encode(temp_data)
    return render(request, 'viewimg.html', {'imagedata': temp_data})
