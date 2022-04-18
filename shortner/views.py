from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        if not Url.objects.filter(link=url).exists():
            uid = str(uuid.uuid4())[:5]
            new_url = Url(link=url,uuid=uid)
            new_url.save()
        else:
            url_details = Url.objects.get(link=url)
            uid = url_details.uuid
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)