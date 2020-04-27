"""
@author: Thomason
@contact: ThomasonZhao@outlook.com 
@create: 2020/4/27 9:14 AM 
"""
from django.urls import include, path
from imgtest import views

urlpatterns = [
    path('save-img/', views.saveImage),
    path('view-img/', views.viewImage)
]
