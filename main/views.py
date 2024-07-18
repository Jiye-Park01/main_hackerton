from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import *
from .models import *
from .serializers import openTimeSerializer

# 열람시간 설정 api
@api_view(['POST'])
def set_open_time(request):
    user = request.user
    serializer = openTimeSerializer(data = request.data)
    if serializer.is_valid():
        open_time, created = openTime.objects.get_or_create(user=user)
        open_time.morning_time = serializer.validated_data['morning_time']
        open_time.night_time = serializer.validated_data['night_time']
        open_time.save()
        return Response({'message': 'Open time set successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 열람시간 수정
def modify_time(request):
    user = request.user
    open_time, created = openTime.objects.get_or_create(user=user, defaults={'morning_time': '06:00:00', 'night_time': '23:00:00'})
    if request.method == 'POST':
        form = OpenTimeForm(request.POST, instance=open_time)
        if form.is_valid():
            form.save()
            return redirect('main:main')
    else:
        form = OpenTimeForm(instance=open_time)
    return render(request, 'main/modify_time.html', {'form': form})

# 메인화면을 렌더링 + 열람시간 띄우기
def main(request):
    user = request.user
    open_time = openTime.objects.filter(user=user).first()
    context = {
        'morning_time': open_time.morning_time if open_time else None,
        'night_time': open_time.night_time if open_time else None,
    }

    today = timezone.now().date()
    user_profile, created = Profile.objects.get_or_create(user=user)
    # 메세지 작성 여부 적용 함수
    user_has_written_message = Message.objects.filter(nick=user_profile, created_at__date=today).exists()

    context['user_has_written_message'] = user_has_written_message

    return render(request, 'main/main.html', context)

# 메시지 열람하기
def message_list(request):
    today = timezone.now().date()
    messages = Message.objects.filter(created_at__date=today)
    return render(request, 'main/message_list.html', {'messages': messages})

# 메세지 작성하기
def message_create(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            user_profile, created = Profile.objects.get_or_create(user=request.user)
            user_profile.nickname = nickname
            user_profile.save()

            message = form.save(commit=False)
            message.nick = user_profile

            message.save()
            return redirect('main:main')
        
    else:
        form = MessageForm()

    return render(request, 'main/message_create.html', {'form': form})

# 메세지 수정하기
def update(request, id):
    message = get_object_or_404(Message, id=id)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            user_profile, created = Profile.objects.get_or_create(user=request.user)
            user_profile.nickname = nickname
            user_profile.save()
            form.save()
            return redirect('main:main')
    else:
        form = MessageForm(instance=message)
    return render(request, 'main/update.html', {'form': form, 'message': message})