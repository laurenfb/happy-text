from django.shortcuts import render

# Create your views here.
def index(request):
    number = "303 478 2060"
    return render(request, 'index.html', {
        'number': number,
    })
