from django.http import HttpResponse
from django.shortcuts import render
from scr.models import Category, Quote, Chat_m
from django.views.generic import FormView
from scr.forms import MyModelForm, Quotation, Chat_f
import os
import threading, time
import random

def dela():
    time.sleep(1)
    pat_1 = os.getcwd() + '/static/xl/a.csv'
    pat_2 = os.getcwd() + '/static/xl/b.csv'
    try:
        os.remove(pat_1)
        print('a.csv deleted')
    except:
        print('a.csv not found')

    try:
        os.remove(pat_2)
        print('b.csv deleted')
    except:
        print('b.csv not found')

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
    sta = os.getcwd() + '/static/xl/a.csv'
    f = open(sta,'w')
    f.write(dataset.csv)
    f.close()
    threadObj = threading.Thread(target=dela)
    threadObj.start()
    return render(request, 'scr/success.html')

def exce(request):
    from scr.admin import Quote_list
    dataset = Quote_list().export()
    sta = os.getcwd() + '/static/xl/b.csv'
    f = open(sta,'w')
    f.write(dataset.csv)
    f.close()
    threadObj = threading.Thread(target=dela)
    threadObj.start()
    return render(request, 'scr/q.html')




## Chat Bot Related

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    word = sentence
    if word.lower() in GREETING_KEYWORDS:
        return random.choice(GREETING_RESPONSES)
    else:
        return ('Greet me')

def chat(request):
    form = Chat_f()
    b = {'line':''}
    b['form'] = form
    if request.method == 'POST':
        form = Chat_f(request.POST)
        if form.is_valid():
            a = request.POST
            sentence = a['say']
            b['line'] = check_for_greeting(sentence)
            form.save(commit=True)
            return render(request, 'scr/chat.html',b)

        else:
            print(form.errors)

    return render(request, 'scr/chat.html',b)
