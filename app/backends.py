from django.contrib.auth.backends import BaseBackend
from app.models import Users
from django.contrib import messages

class USER_Backend(BaseBackend):
    def authenticate(self, request, username=None, password=None, role=None, **kwargs):
        # 自定义的认证逻辑
        try:
            user = Users.objects.get(user_name=username, role=role)
            print(password)
            print(user.password)
            if user.password == password:
                return user
            else:
                messages.error(request, '密码不正确喵')
                return None
        except Users.DoesNotExist:
            messages.error(request, '用户不存在喵')
            return None

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None
