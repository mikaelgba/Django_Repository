from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Wrold in Django seus cornos!")

def hello(request):
    return HttpResponse("<h1> Hello World Seus cornos <h1>")

def hello_name(request,nome):
    return HttpResponse("<h1> Hello World Seu corno {} <h1>".format(nome))

def hello_name_age(request,nome, idade):
    return HttpResponse("<h1> Hello World Seu corno {} de {} <h1>".format(nome, idade))
