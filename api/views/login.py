from django.views import View
from django.http import JsonResponse
from django import forms
from app01.models import UserInfo
from django.contrib import auth


class LoginForms(forms.Form):
    name = forms.CharField(error_messages={'required': '请输入用户名'})
    pwd = forms.CharField(error_messages={'required': '请输入密码'})
    code = forms.CharField(error_messages={'required': '请输入验证码'})

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        user = UserInfo.objects.filter(username=name).first()
        if not user:
            self.add_error('name', '用户名错误')
        return name

    def clean_code(self):
        request = self.request
        code: str = self.cleaned_data['code']
        valid_code: str = request.session.get('valid_code')
        if valid_code.upper() != code.upper():
            self.add_error('code', '验证码错误')
        return code

    def clean(self):
        name = self.cleaned_data.get('name')
        pwd = self.cleaned_data.get('pwd')
        user = auth.authenticate(username=name, password=pwd)
        if not user:
            self.add_error('name', '用户名或密码错误')
        self.cleaned_data['user'] = user
        return self.cleaned_data


def clean_form(form):
    err_dict: dict = form.errors
    err_valid = list(err_dict.keys())[0]
    err_msg = err_dict[err_valid][0]
    return err_valid, err_msg


class LoginView(View):
    def post(self, request):
        res = {
            'code': 344,
            'msg': '登录成功',
            'self': None
        }
        data = request.data
        form = LoginForms(data, request=request)
        if not form.is_valid():
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)
        auth.login(request, form.cleaned_data['user'])
        res['code'] = 0
        return JsonResponse(res)
