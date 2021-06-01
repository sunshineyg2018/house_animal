from django.http import JsonResponse
from django.views import View
from user import models


# 用户注册
class Registered(View):
    def post(self,request):
        name = request.POST.get('user')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        email = request.POST.get('email')
        models.User.objects.create(name=name, password=password,user_type=user_type,email=email)