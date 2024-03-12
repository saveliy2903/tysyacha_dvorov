from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Type_jobs
class application(forms.Form):
    TYPE = [
        (1, 'Освещение территорий'),
        (2, 'Установка навесов, беседок, скамеек, урн'),
        (3, 'Обустройство детской площадки'),
        (4, 'Обустройство спротивной площадки'),
        (5, 'Оборудование зоны тихого отдыха'),
        (6, 'Оборудование (ремонт) тротуаров и проездов'),
        (7, 'Оборудование площадки для хозяйственно-бытовых нужд'),
        (8, 'Оборудование для детей с ОВЗ')
    ]

    quantity_MKD = forms.IntegerField(label="Число МКД", max_value= 10, min_value= 1)
    address = forms.CharField(label="Улица", strip=True)
    population = forms.IntegerField(label="Число жителей", min_value=1)
    yard_area = forms.IntegerField(label="Площадь двора к проектированию", min_value=1)
    percentage_vote = forms.FloatField(label="Голосов от общего числа собственников", min_value=1, max_value=100)
    participated = forms.BooleanField(label="", help_text="Участие в муниципальных программах по благоустройству дворовых территорий")
    type = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TYPE,
        label="Перечень видов работ по благоустройству дворовой территории"
    )
    protocol = forms.CharField(label="Ссылка на протокол общедомового собрания", strip=True)
    CRT = forms.CharField(label="Ссылка на дизайн-проект разработанный АНО 'ЦРТ'", strip=True)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')