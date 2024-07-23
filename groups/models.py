from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# 그룹정보
class Group(models.Model):
    name = models.CharField(max_length=40)
    introduce = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    current_members = models.IntegerField(default=0)
    max_members = models.IntegerField(default=50)

    def __str__(self):
        return self.name
    
# 사용자 가입정보
class Membership(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # group.memberships.all()을 통해 조회가 가능하다.
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    joined_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.profile.user.username} -> {self.group.name}'

