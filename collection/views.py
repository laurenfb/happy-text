from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    number = "303 478 2060"
    return render(request, 'index.html', {
        'number': number,
    })

def sms(request):
    text = '<Response><Message>Hello from your Django app!</Message></Response>'
    response = HttpResponse(text, content_type='text/xml')
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET'
    return response
