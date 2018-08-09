from django import forms

class GuestForm(forms.Form):
    guest_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class' : 'input1'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Phone Number', 'class' : 'input1'}))
    group_size = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'How Many People', 'class' : 'input1'}))
