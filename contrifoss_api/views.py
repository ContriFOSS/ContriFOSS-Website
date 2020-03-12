from django.http import HttpResponse


def index(request):
    return HttpResponse("Contrifoss API is working")
