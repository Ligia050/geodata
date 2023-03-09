from django.urls import path
from . import views

urlpatterns = [ 
path("", views.americanorte),
path("canada", views.canada,name="canada")

]