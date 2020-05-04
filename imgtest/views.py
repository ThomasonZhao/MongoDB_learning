from django.http import HttpResponse
from django.shortcuts import render
from imgtest import models
import base64
# Create your views here.


def saveImage(request):
    print(request.method)
    if request.method == "POST":
        file = request.FILES
        imgtmp = file.get('image', None).read()
        temp = models.ImageModel()
        temp.filename = 'WeChat_img'
        temp.data.put(imgtmp, content_type='image/jpeg')
        temp.save()
        return HttpResponse("---Success---")


def viewImage(request):
    imglist = []
    image = models.ImageModel.objects(filename='WeChat_img')
    print(image)
    for each in image:
        temp_data = each.data.read()
        temp_data = base64.b64encode(temp_data)
        temp_data = bytes.decode(temp_data)
        imglist.append(temp_data)

    return render(request, 'viewimg.html', {'imglist': imglist})
