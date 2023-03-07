from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def americanorte(request):
	return HttpResponse("América do Norte")