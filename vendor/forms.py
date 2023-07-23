from django import forms
from app.models import Product, Category
from ckeditor.fields import CKEditorWidget


class Add_Product_Form(forms.ModelForm):
    vendor_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_vendor'}), required=True, help_text="Vendor name must be unique",)
    total_quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Categories = forms.ModelChoiceField(queryset=Category.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control'}))
    Product_Information = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'Availability': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.TextInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'Discount': forms.TextInput(attrs={'class': 'form-control'}),
            'tax': forms.TextInput(attrs={'class': 'form-control'}),
            'packing_cost': forms.TextInput(attrs={'class': 'form-control'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Categories': forms.Select(attrs={'class': 'form-control'}),
            'Tags': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_vendor_name(self):
        vendor_name = self.cleaned_data.get('vendor_name')
        if Product.objects.filter(vendor_name=vendor_name).exists():
            raise forms.ValidationError("Vendor name already exists.")
        return vendor_name
