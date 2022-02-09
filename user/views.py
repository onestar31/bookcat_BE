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
        User(
            userName = data['userName'],
            userEmail = data['userEmail'],
            userPw = data['userPw'],
        )

        if User.objects.filter(userEmail = data['userEmail']).exists() == True:
            return JsonResponse({"message" : "이미 존재하는 이메일입니다."}, status = 401)

        else:
            User.objects.create(userEmail = data['userEmail'], userName = data['userName'], userPw = data['userPw'])
            return JsonResponse({"message" : "회원으로 가입되셨습니다."}, status = 200)

    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data" : list(users)}, json_dumps_params={'ensure_ascii': False}, status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        # userName = ""
        # uid = ""
        # TODO 쿼리셋으로 데이터 보내주기
        User(
            userEmail = data['userEmail'],
            userPw = data['userPw'],
        )

        if User.objects.filter(userEmail = data['userEmail']).exists() == True:
            userData = User.objects.filter(userEmail = data['userEmail']).values('id','userName')[0]
            print(userData.get('userName'))

            userName = userData.get('userName')
            uid = userData.get('id')

        if User.objects.filter(userEmail = data['userEmail'],  userPw = data['userPw']).exists() == True :
            return JsonResponse({"message": "로그인에 성공하셨습니다.",
                                 "userEmail": data['userEmail'], "uid": uid, "userName":userName}, status = 200)
        else:
            return JsonResponse({"message" : "아이디나 비밀번호가 일치하지 않습니다."}, status = 401)

    def get(self, request):
        user = User.objects.values()
        return JsonResponse({"list" : list(user)}, json_dumps_params={'ensure_ascii': False}, status = 200)


'''
출처
[  https://velog.io/@trequartista/TIL14-Django-회원가입로그인-기능-구현  ]
'''