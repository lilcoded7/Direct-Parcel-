from django.contrib.auth.forms import UserChangeForm
from .models import Package, CustomerRegister
from django import forms 



class Packageform(UserChangeForm):

    senderName = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter sender name',
                'class'      : 'sendername'
            }
        )
    )

    senderEmail = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter sender email',
                'class'      : 'sendername'
            }
        )
    )

    senderContact = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter sender contact',
                'class'      : 'sendername'
            }
        )
    )

    senderLocation = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter sender Location',
                'class'      : 'sendername'
            }
        )
    )

    receiverName = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter receiver name',
                'class'      : 'sendername'
            }
        )
    )

    receiverEmail = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter receiver email',
                'class'      : 'sendername'
            }
        )
    )

    receiverContact = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter receiver contact',
                'class'      : 'sendername'
            }
        )
    )

    receiverLocation = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter receiver Location',
                'class'      : 'sendername'
            }
        )
    )

    
    class Meta:
        model  = Package
        fields = ('senderName', 'senderEmail', 'senderContact', 'senderLocation', 'receiverName', 'receiverEmail', 'receiverContact', 'receiverLocation')


class trackerform(forms.Form):
    id = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter-Tracking-Number',
                'class'      : 'src-bar',       
            }
        )   
    )


class CustomerRegisterform(UserChangeForm):

    fullname = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter receiver Location',
                'class'      : 'sendername'
            }
        )
    )

    country = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter receiver Location',
                'class'      : 'sendername'
            }
        )
    )

    email = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter receiver Location',
                'class'      : 'sendername'
            }
        )
    )

    contact = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter receiver Location',
                'class'      : 'sendername'
            }
        )
    )

    houseaddress = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'Enter receiver Location',
                'class'      : 'sendername'
            }
        )
    )

    

