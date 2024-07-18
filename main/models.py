from django.db import models
from users.models import *
from django.utils import timezone

# 열람시간 저장 모델 + 각 유저마다 시간을 다르게 볼 수 있도록
class openTime(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    morning_time = models.TimeField(default='06:00:00')
    night_time = models.TimeField(default='23:00:00')

    def __str__(self):
        return f"모닝메세지: {self.morning_time}, 나잇메세지: {self.night_time}"

# 메세지 작성 모델
class Message(models.Model):
    nick = models.ForeignKey(Profile, on_delete=models.CASCADE)
    morning_mes = models.CharField(max_length=200)
    night_mes = models.CharField(max_length=200)
    created_at = models.DateTimeField('date published', default = timezone.now)

    def __str__(self):
        return f"{self.morning_mes}, {self.night_mes}"