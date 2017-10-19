from django.http import HttpResponse
    def index(request):
        return　HttpResponse("hello")
    def index2(request):
        return HttpResponse('index2')
