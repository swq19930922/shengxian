from django.shortcuts import render
from df_user.models import *
from df_cart.models import *


def order(request):
    uid = request.session['id']
    user = UserInfo.objects.get(pk=uid)
    cartlist = CartInfo.objects.filter(user_id=uid)
    goods_num = len(cartlist)
    context = {
        'title': '提交订单',
        'user': user,
        'cartlist': cartlist,
        'goods_num': goods_num,
    }
    return render(request, 'df_order/place_order.html', context)
