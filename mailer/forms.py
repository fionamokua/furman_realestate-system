from email import message
from django import forms


#a form class that inherits from Form base class
class EmailForm (forms.Form):
    recipient=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)