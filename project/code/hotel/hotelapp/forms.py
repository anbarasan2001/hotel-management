from django import forms
from hotelapp.models import addroom_modelTable,customer_modelTable
class customer_RegForm(forms.ModelForm):
    class Meta:
        model=customer_modelTable
        fields='__all__'
class addroom_RegForm(forms.ModelForm):
    class Meta:
        model=addroom_modelTable
        fields=['name','no_of_beds']        