from django.db import models
from users.models import *
from django.utils import timezone

# 열람시간 저장 모델
class openTime(models.Model):
    morning_time = models.TimeField()
    night_time = models.TimeField()

    def __str__(self):
        return f"모닝메세지: {self.morning_time}, 나잇메세지: {self.night_time}"

# 메세지 작성 모델
class Message(models.Model):
    morning_mes = models.CharField(max_length=200)
    night_mes = models.CharField(max_length=200)
    created_at = models.DateTimeField('date published', default = timezone.now)
    nick = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.morning_mes}, {self.night_mes}"