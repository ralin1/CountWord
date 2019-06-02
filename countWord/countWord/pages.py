from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Hello world')
def words(request):
    return HttpResponse('Food')
