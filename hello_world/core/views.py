from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def calendario(request):
    return render(request, 'calendario.html')

def faq(request):
    return render(request, 'faq.html')