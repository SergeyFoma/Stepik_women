from django import forms
from women.models import Category, Husband,Women
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

#создаем свой валидатор если нужно многократное использование
# @deconstructible
# class RussianValidator:
#     ALLOWED_CHARS='АБВГДЕЖИСКЛМНОПРСТабвгдежисклмнпрст1234567890-! '
#     code='russian'

#     def __init__(self, message=None):
#         self.message if message else "Должны быть русские символы, дефис и пробел"

#     def __call__(self, value, *args, **kwds):
#         if not (set(value)<=set(self.ALLOWED_CHARS)):
#             raise ValidationError(self.message, code=self.code)

'''class AddPostForm(forms.Form):
    title=forms.CharField(max_length=100,min_length=5,
                          label='Заголовок',
                          widget=forms.TextInput(attrs={"class":"form-input"}),
                          #validators=[RussianValidator()],
                          error_messages={
                              'min_length':'Слишком короткий заголовок',
                              'required':'Без заголовка никак',
                          })
    slug=forms.SlugField(max_length=100,label='URL',
                         validators=[MinLengthValidator(5, message="Минимум 5 символов"),
                                     MaxLengthValidator(100, message='максимум 100 символов')])
    content=forms.CharField(widget=forms.Textarea(attrs={"cols":50,"rows":5}),required=False,label='Контент')
    is_published=forms.BooleanField(label='Статус',initial=True)
    cat=forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Категория не выбрана',label='Категории')
    husband=forms.ModelChoiceField(queryset=Husband.objects.all(),empty_label='Не замужем',label='Муж',required=False)

    #создаем метод валидации для отдельного поля
    def clean_title(self):
        title=self.cleaned_data['title']
        ALLOWED_CHARS='АБВГДЕЖИСКЛМНОПРСТабвгдежисклмнпрст1234567890-! '

        if not (set(title)<=set(ALLOWED_CHARS)):
            raise ValidationError("Должны быть русские символы, дефис и пробел")
        return title'''

    # def clean(self):
    #     cleaned_data=super().clean()
    #     ALLOWED_CHARS="AaQqWwEeRrTtYyUuIiOoPpSsDdFfGgHhJjKkLlMmNnBbVvCcXxZz1234567890-?!$#@_"
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #     if not (set(password1)<=set(ALLOWED_CHARS)):
    #         raise ValidationError("Некорректно введенный пароль.")
    #     if len(password1)<6 or len(password2)<6:
    #         raise ValidationError("Слишком короткий пароль.")
    #     if password1!=password2:
    #         raise ValidationError("Пароли не совпадают.")
    #     return cleaned_data

class AddPostForm(forms.ModelForm):
    cat=forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Категория не выбрана',label='Категории')
    husband=forms.ModelChoiceField(queryset=Husband.objects.all(),empty_label='Не замужем',label='Муж',required=False)
    class Meta:
        model=Women
        #fields='__all__'
        fields=['title','slug','content','is_published','cat','tags','husband']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':50,'rows':5})
        }
        labels={'slug':'URL'}

    def clean_title(self):
        title=self.cleaned_data['title']
        if len(title)>10:
            raise ValidationError("Длина превышает 10 символов")
        return title


class UploadFileForm(forms.Form):
    file=forms.FileField(label="Файл")