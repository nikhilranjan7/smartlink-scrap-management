from scr.models import Category
from django import forms

Department = (
    ('rma','RMA'),
    ('production', 'PRODUCTION'),
    ('warehouse', 'WAREHOUSE'),
    ('maintenance', 'MAINTENANCE'),
)

Type = (
    ('hazardous', 'HAZARDOUS'),
    ('e-waster', 'E-WASTE'),
    ('metals', 'METALS'),
    ('paper', 'PAPER'),
    ('plastic', 'PLASTIC'),
)

class MyModelForm(forms.ModelForm):
    department = forms.ChoiceField(choices=Department,required=True,
                                    help_text="Department")
    waste_type = forms.ChoiceField(choices=Type, required=True,
                                    help_text="Type of Waste")
    description = forms.CharField(max_length=1000,
                                    help_text="Description")
    class Meta:
        model = Category
        fields = ['department', 'waste_type', 'description']
