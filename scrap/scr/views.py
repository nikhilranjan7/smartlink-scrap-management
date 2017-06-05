from django.http import HttpResponse
from django.shortcuts import render
from scr.models import Category, Quote, Random_m
from django.views.generic import FormView
from scr.forms import MyModelForm, Quotation, Random_f

def index(request):
    context_dict = {'boldmessage': "Scrap Management"}

    return render(request, 'scr/index.html', context=context_dict)

def add(request):
    form = MyModelForm()

    if request.method == 'POST':
        form = MyModelForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print(form.errors)

    return render(request, 'scr/add.html', {'form': form})

def quotes(request):
    forma = Quotation()

    if request.method == 'POST':
        forma = Quotation(request.POST)

        if forma.is_valid():
            forma.save(commit=True)
            return index(request)

        else:
            print(forma.errors)

    return render(request, 'scr/quote.html', {'form': forma})

def excel(request):
    form = Random_f()
    if request.method == 'POST':
        form = Random_f(request.POST)

        if form.is_valid():
            form.save(commit=True)

            import requests, sys, webbrowser, bs4

            print('Googling...')
            res = requests.get('https://google.com/search?q=Smartlink')
            res.raise_for_status()

            # Retrieve top search result links.
            soup = bs4.BeautifulSoup(res.text, "html.parser")

            # Open a browser tab for each result.
            linkElems = soup.select('.r a')
            numOpen = min(5, len(linkElems))
            for i in range(numOpen):
                webbrowser.open('https://google.com/' + linkElems[i].get('href'))
                
            return render(request, 'scr/success.html', {'form': form})

        else:
            print(form.errors)

    return render(request, 'scr/success.html', {'form': form})
