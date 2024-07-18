from django import forms
from .models import *

# 열람시간 폼
class OpenTimeForm(forms.ModelForm):
    class Meta:
        model = openTime
        fields = ['morning_time', 'night_time']
        widgets = {
            'morning_time': forms.TimeInput(attrs={'type': 'time'}),
            'night_time': forms.TimeInput(attrs={'type': 'time'}),
        }

# 메세지 폼
class MessageForm(forms.ModelForm):
    nickname = forms.CharField(label="닉네임", max_length=40)

    class Meta:
        model = Message
        fields = ['morning_mes', 'night_mes', 'nickname']
        labels = {
            'morning_mes': '아침메세지',
            'night_mes': '밤메세지',
        }