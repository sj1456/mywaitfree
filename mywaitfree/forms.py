from django import forms

class GuestForm(forms.Form):
    guest_name = forms.CharField(label='Your Name', max_length=100)
    phone_number = forms.CharField(label='Phone Number', max_length=100)