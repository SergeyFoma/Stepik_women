from django import forms
from women.models import Category, Husband

class AddPostForm(forms.Form):
    title=forms.CharField(max_length=100,label='Заголовок',widget=forms.TextInput(attrs={"class":"form-input"}))
    slug=forms.SlugField(max_length=100,label='URL')
    content=forms.CharField(widget=forms.Textarea(attrs={"cols":50,"rows":5}),required=False,label='Контент')
    is_published=forms.BooleanField(label='Статус',initial=True)
    cat=forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Категория не выбрана',label='Категории')
    husband=forms.ModelChoiceField(queryset=Husband.objects.all(),empty_label='Не замужем',label='Муж',required=False)