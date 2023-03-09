from django.shortcuts import render

# Create your views here.


def americasul(request):
	return render (request, 'sul.html')

def brasil(request):
	return render (request, 'brasil.html')	

def peru(request):
	return render (request, 'peru.html')	

def chile(request):
	return render (request, 'chile.html')	

def equador(request):
	return render (request, 'equador.html')	