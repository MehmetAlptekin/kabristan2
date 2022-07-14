from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

        
class DetayCreate(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'İsminiz'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Soy İsminiz'}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control rounded-0 w-100', 'placeholder': 'Doğum Tarihiniz' ,'required': 'required' , 'rows':6,}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Numaranız'}))
    image = forms.ImageField()
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Şehir'}))

    class Meta:
        model = KisiDetay
        fields = ['name','surname','birth_date','phone_number','image','city']

    def clean(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            surname = self.cleaned_data['surname']
            birth_date = self.cleaned_data['birth_date']
            phone_number = self.cleaned_data['phone_number']
            image = self.cleaned_data['image']
            city = self.cleaned_data['city']

        
class blogForm(forms.ModelForm):
    blog_title = forms.CharField(max_length=550, widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Blog Başlık'}))
    category = forms.ModelChoiceField(queryset=BlogCategory.objects.all(),widget=forms.Select(attrs={'class':'selectpicker form-control ', 'data-live-search':'true',}))
    blog_description = forms.CharField(max_length=100000,widget=CKEditorWidget(attrs={'class':'form-control rounded-0 w-100', 'placeholder': 'Blog Açıklama' ,'required': 'required' , 'rows':6,}))
    class Meta:
        model = blogBilgi
        fields = ['blog_title','blog_description','image','category']