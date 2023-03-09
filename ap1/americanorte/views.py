from django.shortcuts import render

def americanorte(request):
	return render (request, 'norte.html')

def canada(request):
	return render (request, 'canada.html')
