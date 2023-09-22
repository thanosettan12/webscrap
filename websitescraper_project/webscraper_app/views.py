from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from .models import Links


# Create your views here.
def home(request):
    if request.method == "POST":
        enter_link = request.POST.get('page', '')
        urls = requests.get(enter_link)
        beauty = BeautifulSoup(urls.text, 'html.parser')

        for link in beauty.find_all('a'):
            link_address = link.get('href')
            link_string = link.string
            Links.objects.create(address=link_address, string_name=link_string)
        return redirect('/')
    else:
        data_values = Links.objects.all()

    return render(request, 'home.html', {'data_values': data_values})


def clear_table(request):
    Links.objects.all().delete()
    return redirect('/')