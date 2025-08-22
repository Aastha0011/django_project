from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My First Django project!</h1>")

# Create your views here.
