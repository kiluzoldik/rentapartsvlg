from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User
from datetime import datetime
import calendar


class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
        )

    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

class UserIdentifierForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'full_name',
            'phone_number',
            'email',
            'birthday',
            'series_and_number',
            'issued_by',
            'date_of_issue',
            'department_code',
            'registration_address'
        )

    full_name = forms.CharField()
    phone_number = forms.CharField()
    email = forms.EmailField()
    series_and_number = forms.CharField()
    department_code = forms.CharField()
    birthday = forms.CharField()
    date_of_issue = forms.CharField()

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        russian_alphabet = [chr(i) for i in range(ord('А'), ord('Я') + 1)] + [chr(i) for i in range(ord('а'), ord('я') + 1)] + [' ']  
        if len(full_name) > 250:
            print(len(full_name.split(' ')))
            raise forms.ValidationError('Превышен лимит символов (Максимум: 250)')
        elif len(full_name.split(' ')) < 3 or len(full_name.split(' ')) > 3:
            raise forms.ValidationError('Некорректно введено ФИО (Пример: Иванов Иван Иванович)')
        elif len(full_name) != len([simbol for simbol in full_name if simbol in russian_alphabet]):
            raise forms.ValidationError('Некорректно введены символы (Вводить можно только буквы русского алфавита)')
        else:
            for i in full_name.split(' '):
                if i[0].isupper() and i[1:].islower():
                    continue
                else:
                    raise forms.ValidationError('Фамилия, имя и отчество должны начинаться с большой буквы, все остальные буквы маленькие')
        
        return full_name
    
    def clean_series_and_number(self):
        series_and_number = self.cleaned_data['series_and_number']
        numbers = [str(i) for i in range(0, 10)] + [' ']
        if len(series_and_number) > 11:
            raise forms.ValidationError('Превышен лимит символов (Максимум: 10)')
        elif len(series_and_number.split(' ')) < 2 or \
        0 < len(series_and_number.split(' ')[0]) < 4 or \
        0 < len(series_and_number.split(' ')[1]) < 6:
            raise forms.ValidationError('Некорректно введены серия и номер (Пример: 1234 567890)')
        elif len(series_and_number) != len([num for num in series_and_number if num in numbers]):
            raise forms.ValidationError('Введены запрещённые символы (Используйте цифры и знак пробела)')
        
        return series_and_number
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if 0 < len(phone_number) < 11 or len(phone_number) > 11:
            raise forms.ValidationError('Номер телефона введён неверно')
        elif not phone_number.isdigit():
            raise forms.ValidationError('Недопустимые символы (Пример: 81234567890)')
        elif not phone_number.startswith('8') and not phone_number.startswith('7'):
            raise forms.ValidationError('Номер телефона должен начинаться с "7" или "8"')
        
        return phone_number
    
    def clean_department_code(self):
        department_code = self.cleaned_data['department_code']
        if len(department_code) > 7 or 0 < len(department_code) < 7 or '-' not in department_code:
            raise forms.ValidationError('Код подразделения введен неверно')
        elif not department_code.split('-')[0].isdigit() or not department_code.split('-')[1].isdigit():
            raise forms.ValidationError('Недопустимые символы (Пример: 123-456)')
        
        return department_code
    
    def clean_birthday(self):
        birthday = self.cleaned_data['birthday']
        day_mnth_year = birthday.split('.')
        if 0 < len(birthday) < 10 or len(birthday) > 10 or birthday.count('.') < 2:
            raise forms.ValidationError('Неверное количество символов (Пример: 01.01.2001)')
        elif not day_mnth_year[0].isdigit() or not day_mnth_year[1].isdigit() or not day_mnth_year[2].isdigit():
            raise forms.ValidationError('Некорректные символы')
        elif int(day_mnth_year[0]) > 31 or int(day_mnth_year[0]) == 0:
            raise forms.ValidationError('Некорректный день месяца')
        elif int(day_mnth_year[1]) > 12 or int(day_mnth_year[1]) == 0:
            raise forms.ValidationError('Некорректный месяц')
        elif datetime.strptime(birthday, '%d.%m.%Y') > datetime.now():
            raise forms.ValidationError('Дата рождения не должна превышать текущего времени')
        
        return birthday
    
    def clean_date_of_issue(self):
        date_of_issue = self.cleaned_data['date_of_issue']
        day_mnth_year = date_of_issue.split('.')
        if 0 < len(date_of_issue) < 10 or len(date_of_issue) > 10 or date_of_issue.count('.') < 2:
            raise forms.ValidationError('Неверное количество символов (Пример: 01.01.2001)')
        elif not day_mnth_year[0].isdigit() or not day_mnth_year[1].isdigit() or not day_mnth_year[2].isdigit():
            raise forms.ValidationError('Некорректные символы')
        elif int(day_mnth_year[0]) > 31 or int(day_mnth_year[0]) == 0 or \
        (calendar.isleap(int(day_mnth_year[2])) and int(day_mnth_year[0]) > 29) or \
        (not calendar.isleap(int(day_mnth_year[2])) and int(day_mnth_year[0]) > 28):
            raise forms.ValidationError('Некорректный день месяца')
        elif int(day_mnth_year[1]) > 12 or int(day_mnth_year[1]) == 0:
            raise forms.ValidationError('Некорректный месяц')
        elif int(day_mnth_year[2]) < 1900:
            raise forms.ValidationError('Некорректный год')
        elif datetime.strptime(date_of_issue, '%d.%m.%Y') > datetime.now():
            raise forms.ValidationError('Дата выдачи не должна превышать текущего времени')
        
        return date_of_issue