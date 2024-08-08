from django.http import HttpResponse # type: ignore

def text(request):
    return HttpResponse("Hello world")
