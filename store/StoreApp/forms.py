from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Articles, User, Purchase
from django.forms import ModelForm, TextInput, Textarea, NumberInput, IntegerField


class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        # fields = ['name', 'text']
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product name'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Product description'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product price'
            }),
            'amount': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Amount of product'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class LoginUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ('buyer', 'product', 'input_amount', 'final_price')
        # fields = '__all__'
        widgets = {
            'input_amount': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'input_amount'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
