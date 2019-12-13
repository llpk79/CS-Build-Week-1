from django.http import HttpResponse


def index(request):
    return HttpResponse('Wait, now this is the app!!??')
