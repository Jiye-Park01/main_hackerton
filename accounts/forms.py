from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 회원가입 폼
class SignupForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    nickname = forms.CharField(label="닉네임", max_length=40)

    class Meta():
        # AUTH_USER_MODEL이라고 settings.py에 정의한 user모델 가져온다는 의미
        model = User
        fields = [ "nickname", "username", "email"]