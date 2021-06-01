from django.db import models


class User(models.Model):
    """用户信息"""
    # 用户名
    name = models.CharField(max_length=12)
    # 年龄
    age = models.IntegerField(null=True)
    # 身份证
    id_card = models.CharField(max_length=18,null=True)
    # 用户电话
    tel = models.IntegerField(max_length=13,null=True)
    # 创建时间
    date = models.DateTimeField()
    # 真实姓名
    card_name = models.CharField(max_length=15,null=True)
    # 是否实名标识
    real_type = models.IntegerField(max_length=2)
    # 密码
    password = models.CharField(max_length=15)
    # 用户类别
    user_type = models.IntegerField()
    # 邮箱
    email = models.EmailField()



