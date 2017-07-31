from django.shortcuts import render

# Create your views here.

def home(request):
	context = {}
	return render(request, 'index.html', context)

def cms_page(request):
	context = {}
	return render(request, 'cms_index.html', context)