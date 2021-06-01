from django.db import models

from user.models import User


class Order_info(models.Model):
    """订单信息"""
    # 订单ID
    order_id = models.CharField(max_length=30)
    # 付款金额
    money = models.FloatField()
    # 支付状态
    pay_status = models.IntegerField()
    # 订单备注
    order_data = models.CharField(max_length=150,null=True)
    # 订单创建时间
    date = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


