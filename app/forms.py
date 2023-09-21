from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, CustomUser, Vendor


class CustomerSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'name',
                  'address', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user, name=self.cleaned_data.get(
            'name'), address=self.cleaned_data.get('address'))
        return user


class VendorSignUpForm(UserCreationForm):

    name = forms.CharField(required=True)
    age = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'name', 'address', 'age',
                  'password1', 'address', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        user.save()
        vendor = Vendor.objects.create(user=user, name=self.cleaned_data.get(
            'name'), age=self.cleaned_data.get('age'), address=self.cleaned_data.get('address'))
        return user
