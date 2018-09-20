from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>BLUE CONTAINER</h1>')