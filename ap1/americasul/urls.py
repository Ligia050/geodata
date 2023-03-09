from django.urls import path
from . import views

urlpatterns = [ 
path("", views.americasul,name="americasul"),
path("brasil", views.brasil,name="brasil"),
path("peru", views.peru,name="peru"),
path("equador", views.equador,name="equador"),
path("chile", views.chile,name="chile")
]