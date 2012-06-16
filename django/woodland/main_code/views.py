# Create your views here.
from django.http import HttpResponse

def hello(request):
    print request
    return HttpResponse("Hello, main woodland")
