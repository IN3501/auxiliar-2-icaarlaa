from django.shortcuts import render

# Create your views here.
def index(request): #cargar la pagina que esta en direccion charli_app/index
	return render(request, 'charli_app/index.html')

def pestaña(request):
	return render(request, 'charli_app/pestaña.html')

def p1(request):
	return render(request, 'charli_app/p1.html')


