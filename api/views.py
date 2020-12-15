from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from api.forms import UserInfo,Loginform
import requests
import uuid

class UserLonginView(View):
    template_name = 'login.html'
    form_class = Loginform
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        if request.session.has_key('token'):
            return redirect('data')
        else:
            form = self.form_class(initial=self.initial)

            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.data
        
            payload = {
                "username": data.get('email'),
                "password": data.get('password')
            }

            url = 'https://recruitment.fisdev.com/api/login/'
            res = requests.post(url, json=payload, )
            data_json = res.json()

            if res.status_code == 200:
                request.session['token'] = data_json['token']
                print(request.session['token'])
                messages.success(request, 'Login Successfully..')
                return redirect('data')
                
            else:
                messages.error(request, data_json['message'])
                return redirect('login')
        else:
            return redirect('login')


class UserLogoutView(View):
   def dispatch(self, request, *args, **kwargs):
        if request.session.has_key('token'):
            del request.session['token']
            messages.error(request, 'Logout Successfully!!')
            return redirect('login')
        else:
            return redirect('login')

class DataInputView(View):
    template_name = 'Submit.html'
    form_class = UserInfo
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        if request.session.has_key('token'):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            messages.warning(request, 'You have to login for submit your data..')
            return redirect('login')

    def post(self, request, *args, **kwargs):
        print(self.request.session['token'])
        if request.session.has_key('token'):
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                data = form.data
                immutable = data._mutable
                data._mutable = True
                data['tsync_id'] = str(uuid.uuid1())
                data['cv_file'] = {'tsync_id': str(uuid.uuid1())}
                data._mutable = immutable

              
                head = {
                    'content-type': 'application/json',
                    'Authorization': 'Token ' + self.request.session['token'],
                }
           
                url = 'https://recruitment.fisdev.com/api/v1/recruiting-entities/'

            
                BT = requests.post(url, json=data, headers=head)
                data_json = BT.json()

             
                file_headers = {
                    'Content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW',
                    'Authorization': 'Token ' + self.request.session['token'],
                }
                url = 'https://recruitment.fisdev.com/api/file-object/{}/'.format(data_json['cv_file']['id'])
                btr = requests.put(url, data={'file': self.request.FILES['file']}, headers=file_headers)
                data_json = btr.json()
                print(data_json)
                if btr.status_code == 200:
                    messages.success(request, 'Data Submitted Successfully...')
                    return redirect('data')
                else:
                    messages.error(request, data_json['message'])
            else:
                return redirect('data')
        else:
            return redirect('login')

    
