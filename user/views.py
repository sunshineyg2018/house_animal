from django.http import JsonResponse
from django.views import View
from user import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# 用户注册
@method_decorator(csrf_exempt, name='dispatch')
class Registered(View):
    def post(self, request):
        name = request.POST.get('user')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        email = request.POST.get('email')
        if name and password and user_type and email is not None:
            models.User.objects.create(name=name,
                                       password=password,
                                       user_type=user_type,
                                       email=email,
                                       activation_tag=0,
                                       )
        return JsonResponse({"code":20005,"msg":"请提交完整的数据"})


