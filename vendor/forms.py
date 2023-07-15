from django import forms
from app.models import Product, Category


class Add_Product_Form(forms.ModelForm):
    vendor_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_vendor'}), required=True, help_text="Vendor name must be unique",)
    total_quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Categories = forms.ModelChoiceField(queryset=Category.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = '__all__'

    def clean_vendor_name(self):
        vendor_name = self.cleaned_data.get('vendor_name')
        if Product.objects.filter(vendor_name=vendor_name).exists():
            raise forms.ValidationError("Vendor name already exists.")
        return vendor_name
