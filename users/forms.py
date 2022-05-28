from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import CardDetails
from PIL import Image
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
  
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class CardDetailsForm(forms.ModelForm):
    class Meta:
        model = CardDetails
        fields = ['name_on_card','cc_number','cc_expiry','cc_code','face_id']
