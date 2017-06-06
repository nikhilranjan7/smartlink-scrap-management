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
    from scr.admin import Category_list
    dataset = Category_list().export()

    f = open('/Users/nikhilranjan/Desktop/smartlink/scrap/static/xl/a.csv','w')
    f.write(dataset.csv)
    t = 'static/xl/a.csv'
    return render(request, t)
