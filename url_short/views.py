from django.shortcuts import render
from .models import URLShort


def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        short_url_obj, created = URLShort.objects.get_or_create(url=url)
        return render(request,'shortened.html',{'short_url':short_url_obj})
    return render(request,'home.html')