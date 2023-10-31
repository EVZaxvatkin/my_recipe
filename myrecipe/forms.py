from django import forms
from django.contrib.auth.models import User
from django.forms import Textarea, TextInput, NumberInput
from .models import Recipe, Category


CATEGORY = (
        ('салаты и закуски', 'Салаты и закуски'),
        ('супы', 'Супы'),
        ('вторые блюда. мясо', 'Вторые блюда. Мясо'),
        ('вторые блюда. птица', 'Вторые блюда. Птица'),
        ('вторые блюда. рыба и морепродукты', 'Вторые блюда. Рыба и морепродукты'),
        ('гарниры и соусы', 'Гарниры и соусы'),
        ('хлеб и выпечка', 'Хлеб и выпечка'),
        ('десерты', 'Десерты'),
        ('напитки. алкоголь', 'Напитки. Алкоголь'),
        ('напитки. без алкоголя', 'Напитки. Без алкоголя')
)



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'steps', 'cooking_time', 'image']
        widgets = {
            'name': TextInput(attrs={'style': 'width: 100%'}),
            'description': Textarea(attrs={'style': 'width: 100%'}),
            'steps': Textarea(attrs={'style': 'width: 100%'}),
            'cooking_time': NumberInput(attrs={'style': 'width: 100%'})
        }


class CookingForm(forms.Form):
    name = forms.CharField(label='Название', max_length=50, required=False,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите название рецепта',
                                      'required': 'True'}))

    category = forms.CharField(label='Категория',
                               required=False,
                               widget=forms.Select(attrs={'required': 'True'}, choices=CATEGORY))

    description = forms.CharField(label='Описание',
                                  max_length=500,
                                  required=False,
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control',
                                             'placeholder': 'Введите описание рецепта',
                                             'required': 'True'}))

    steps = forms.CharField(label='Этапы приготовления',
                            required=False,
                            max_length=10000,
                            widget=forms.Textarea(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Введите шаги приготовления',
                                       'required': 'True'}))

    cooking_time = forms.IntegerField(label='Время приготовления', required=False,
                                      widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                      'required': 'True'}))

    image = forms.ImageField(label='Фото блюда', required=False, widget=forms.FileInput(attrs={'required': 'True'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=65)
    password = forms.CharField(label='Пароль', max_length=65, widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)
        labels = {
            'username': 'Имя пользователя'
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']