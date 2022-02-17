import json

from django.views import View
from django.http import JsonResponse

from django.http import HttpResponse

from .models import User

def index(request):
    return HttpResponse("user 기본 페이지")

class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        userName = data['userName']
        userEmail = data['userEmail']
        userPw = data['userPw']
        User(
            userName = userName,
            userEmail = userEmail,
            userPw = userPw,
        )

        if User.objects.filter(userEmail=userEmail).exists():
            return JsonResponse({"message" : "이미 존재하는 이메일입니다."}, json_dumps_params={'ensure_ascii': False}, status = 401)

        else:
            User.objects.create(userEmail = userEmail, userName = userName, userPw = userPw)
            return JsonResponse({"message" : "회원으로 가입되셨습니다."}, json_dumps_params={'ensure_ascii': False}, status = 200)

    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data" : list(users)}, json_dumps_params={'ensure_ascii': False}, status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        userEmail = data['userEmail']
        userPw = data['userPw']
        User(
            userEmail = userEmail,
            userPw = userPw,
        )

        if User.objects.filter(userEmail=userEmail).exists():
            userData = User.objects.filter(userEmail = userEmail).values('id','userName')[0]
            print(userData.get('userName'))

            userName = userData.get('userName')
            uid = userData.get('id')

        if User.objects.filter(userEmail=userEmail, userPw=userPw).exists():
            return JsonResponse({"message": "로그인에 성공하셨습니다.",
                                 "userEmail": userEmail, "uid": uid, "userName":userName}, status = 200)
        else:
            return JsonResponse({"message" : "아이디나 비밀번호가 일치하지 않습니다."}, json_dumps_params={'ensure_ascii': False}, status = 401)

    def get(self, request):
        user = User.objects.values()
        return JsonResponse({"list" : list(user)}, json_dumps_params={'ensure_ascii': False}, status = 200)

class ChangePw(View):
    def patch(self, request):
        data = json.loads(request.body)
        newPw = data['newPw']
        userEmail = data['userEmail']
        userPw = data['userPw']
        User(
            userEmail = userEmail,
            userPw = userPw
        )

        if User.objects.filter(userEmail=userEmail, userPw=userPw).exists():
            userData = User.objects.filter(userEmail = userEmail)
            # userData.update(userPw=newPw)
            userData.update(userPw=newPw)

            return JsonResponse({"message": "비밀번호가 변경되었습니다."}, json_dumps_params={'ensure_ascii': False}, status=200)
        else:
            return JsonResponse({"message" : "기존 비밀번호가 올바르지 않습니다."}, json_dumps_params={'ensure_ascii': False}, status=401)

'''
출처
[  https://velog.io/@trequartista/TIL14-Django-회원가입로그인-기능-구현  ]
https://jinmay.github.io/2020/05/13/django/django-queryset-update/
https://tutorial.djangogirls.org/ko/django_orm/
'''