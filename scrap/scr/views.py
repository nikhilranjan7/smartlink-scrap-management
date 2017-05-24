from django.http import HttpResponse
from django.shortcuts import render
from scr.models import Category
from django.views.generic import FormView
from scr.forms import MyModelForm

def index(request):
    context_dict = {'boldmessage': "Scrap Management"}

    return render(request, 'scr/index.html', context=context_dict)

class Scrap_details(FormView):
    model = Category
    form_class = MyModelForm
    template_name = 'scr/add.html'
    success_url = 'scr/success.html'

    def form_valid(self, form):
        return HttpResponse("<a href=''>You are wasting so much !!</a>")

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
