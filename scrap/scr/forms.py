from scr.models import Category, Quote, Random_m
from django import forms

Company = (
    ('Smartlink Network Systems Ltd.','Smartlink Network Systems Ltd.'),
    ('Digisol Systems Ltd.', 'Digisol Systems Ltd.'),
    ('Synegra EMS Ltd.', 'Synegra EMS Ltd.'),
    ('Telesmart SCS Ltd.', 'Telesmart SCS Ltd.'),
)

Department = (
    ('hr & admin','HR & Admin'),
    ('purchase','Purchase'),
    ('rm stores','RM Stores'),
    ('synegra production', 'Synegra Production'),
    ('logistics & warehouse', 'Logistics & Warehouse'),
    ('commercial', 'Commercial'),
    ('accounts','Accounts'),
    ('legal','Legal'),
    ('s-tac','S-TAC'),
    ('it','IT'),
    ('qa','QA'),
    ('engineering','Engineering'),
    ('telesmart-production','Telesmart-Production'),
)

Type = (
    ('aging material','Aging Material'),
    ('hazardous', 'Hazardous'),
    ('e-waste', 'E-Waste'),
    ('metals', 'Metals'),
    ('paper', 'Paper'),
    ('plastic', 'Plastic'),
    ('furniture','Furniture'),
    ('machinery','Machinery'),
)

class MyModelForm(forms.ModelForm):
    company = forms.ChoiceField(choices=Company,
                 required=True, help_text="Company")
    department = forms.ChoiceField(choices=Department,required=True,
                                    help_text="Department")
    waste_type = forms.ChoiceField(choices=Type, required=True,
                                    help_text="Type of Waste")
    description = forms.CharField(max_length=1000,
                                    help_text="Description")
    class Meta:
        model = Category
        fields = ['company','department', 'waste_type', 'description']

class Quotation(forms.ModelForm):
    name = forms.CharField(max_length=100,required=True,help_text="Name")
    contact_info = forms.CharField(max_length=100,required=True,help_text="Contact Information")
    item = forms.CharField(max_length=100,required=True,help_text="Item")
    quantity = forms.CharField(max_length=100,required=True,help_text="Quantity")
    price = forms.CharField(max_length=100,required=True,help_text="Price quoted")
    additional_info = forms.CharField(max_length=1000,help_text="Additional Information")

    class Meta:
        model = Quote
        fields = ['name', 'contact_info', 'item', 'quantity', 'price', 'additional_info']

class Random_f(forms.ModelForm):
    fill = forms.CharField(max_length=100, help_text="Random Things")

    class Meta:
        model = Random_m
        fields = ['fill',]
