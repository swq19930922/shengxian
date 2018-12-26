from django.shortcuts import render, redirect
from df_user.login_decorator import login
from django.http.response import JsonResponse
from .models import *


# 购物车
@login
def cart(request):
    uid = request.session['id']
    mycart = CartInfo.objects.filter(user_id=uid)
    context = {
        'title': '购物车',
        'mycart': mycart,
    }
    return render(request, 'df_cart/cart.html', context)


# 添加商品
@login
def add_goods(request, gid, gcount):
    uid = request.session['id']
    cartlist = CartInfo.objects.filter(user_id=uid, goods_id=int(gid))
    if len(cartlist) > 0:
        mycart = cartlist[0]
        mycart.count += int(gcount)
    else:
        mycart = CartInfo()
        mycart.user_id = uid
        mycart.goods_id = int(gid)
        mycart.count = int(gcount)
    mycart.save()
    return JsonResponse({'count': mycart.count})
    # return redirect('/cart/')


# 删除商品
def delete_goods(request, cid):
    try:
        if request.is_ajax():
            cart = CartInfo.objects.get(pk=int(cid))
            cart.delete()
            data = {'ok': 1}
    except Exception as e:
        data = {'ok': 1, 'e': e}
    return JsonResponse(data)
    # cart = CartInfo.objects.get(pk=int(cid))
    # cart.delete()
    # data = {'ok': 1}
    # return JsonResponse(data)


# 修改商品数量
def edit_goods(request, cid, num):
    try:
        if request.is_ajax:
            cart = CartInfo.objects.get(pk=int(cid))
            cart.count = int(num)
            cart.save()
            data = {'ok': 1}
    except Exception as e:
        data = {'ok': 1, 'e': e}
    # return JsonResponse(data)
    return data






