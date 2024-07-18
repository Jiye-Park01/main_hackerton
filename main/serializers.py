from django import forms
from rest_framework import serializers
from .models import openTime


# 직렬화: json 타입으로 모델을 변환
# 참고: https://devkor.tistory.com/entry/03-Django-Rest-Framework-Serializer-View-%EA%B0%9C%EB%85%90-%EC%9D%B5%ED%9E%88%EA%B8%B0
class openTimeSerializer(serializers.ModelSerializer):
    class Meta():
        model = openTime
        fields = ['morning_time', 'night_time']
        widgets = {
            'morning_time': forms.TimeInput(attrs={'type': 'time'}),
            'night_time': forms.TimeInput(attrs={'type': 'time'}),
        }