from django.urls import path
from . import views

urlpatterns = [ path("", views.americanorte,name="americanorte")]