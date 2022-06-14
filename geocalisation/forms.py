from django import forms

class distanceForm(forms.Form):
    destinationA_lat = forms.IntegerField()
    destinationA_lon = forms.IntegerField()
    destinationB_lat = forms.IntegerField()
    destinationB_lon = forms.IntegerField()
