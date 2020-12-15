from django import forms

class Loginform(forms.Form):
    email = forms.CharField(max_length=200)
    password = forms.CharField(max_length=20)

job_selection=( ("Backend","Backend"),("Mobile","Mobile"), )

class UserInfo(forms.Form):
    name = forms.CharField(widget=forms.TextInput( attrs={ 'class':'form-control'} ),max_length=256, required=True)
    email = forms.CharField(widget=forms.EmailInput( attrs={ 'class':'form-control'} ),max_length=256, required=True)
    phone = forms.CharField(widget=forms.TextInput( attrs={ 'class':'form-control'} ),max_length=14, required=True)
    full_address = forms.CharField(widget=forms.Textarea( attrs={ 'class':'form-control'} ),max_length=512, required=True)
    name_of_university = forms.CharField(widget=forms.TextInput( attrs={ 'class':'form-control'} ),max_length=256, required=True)
    graduation_year = forms.CharField(widget=forms.TextInput( attrs={ 'min':'2015','max': '2020','type': 'number'} ),label='Graduation Year', required=False)
    cgpa = forms.DecimalField(label='Cgpa', max_value=4, min_value=2, decimal_places=2, required=False )
    experience_in_months = forms.CharField( widget=forms.NumberInput(attrs={ 'class': 'form-control', 'min':0 ,'max': 100,}), required=True)
    current_work_place_name = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}),max_length=256, required=True)
    applying_in = forms.ChoiceField(choices=job_selection, required=True)
    expected_salary = forms.CharField(label='Salary', widget=forms.TextInput(attrs={'min':'15000','max': '60000','type': 'number'}),required=False)
    field_buzz_reference = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}),max_length=256, required=True)
    github_project_url = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}),max_length=512, required=True)
    file = forms.FileField(widget=forms.FileInput(attrs={'accept': 'application/pdf', }))


