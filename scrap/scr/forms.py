from scr.models import Category, Quote, trxn_m
from django import forms
import datetime

Location = (
    ('goa','Goa'),
    ('mumbai','Mumbai'),
    ('bangalore','Bangalore'),
)

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
    time = forms.CharField(widget=forms.HiddenInput(), required=False)
    location = forms.ChoiceField(choices=Location,
                 help_text="Location")
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
        fields = ['company','department', 'waste_type', 'description','location','time']

class Quotation(forms.ModelForm):
    time = forms.CharField(widget=forms.HiddenInput(), required=False)
    location = forms.ChoiceField(choices=Location,
                 help_text="Location of the Scrap generating Company")
    name = forms.CharField(max_length=100,required=True,help_text="Name")
    contact_info = forms.CharField(max_length=100,required=True,help_text="Contact Information")
    item = forms.CharField(max_length=100,required=True,help_text="Item")
    quantity = forms.CharField(max_length=100,required=True,help_text="Quantity")
    price = forms.CharField(max_length=100,required=True,help_text="Price quoted")
    additional_info = forms.CharField(max_length=1000,help_text="Additional Information")
    certificates = forms.URLField(max_length=200, help_text="Google drive link to your authorized license", required=False)

    class Meta:
        model = Quote
        fields = ['name', 'contact_info', 'item', 'quantity', 'price', 'additional_info','location', 'time', 'certificates']



class trxn_f(forms.ModelForm):

    date = forms.DateField(initial=datetime.date.today, help_text="Date")
    location = forms.ChoiceField(choices=Location,
               help_text="Location of the Scrap generating Company")
    items_description = forms.CharField(max_length=1000,help_text="Item Description", widget=forms.Textarea(attrs={'rows':'5', 'width': '100%'}))
    purchasing_party = forms.CharField(max_length=1000, help_text="Purchasing Party")
    selling_price = forms.CharField(max_length=1000, help_text="Price")

    class Meta:
      model = trxn_m
      fields = ['date','location', 'items_description', 'purchasing_party','selling_price']
