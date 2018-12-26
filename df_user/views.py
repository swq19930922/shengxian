from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *
from hashlib import sha1
from . import login_decorator


# 注册
def register(request):
    context = {'title': '注册'}
    return render(request, 'df_user/register.html', context)


# 注册处理
def register_handle(request):
    # 接收用户请求
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    count = UserInfo.objects.filter(uname=uname).count()
    # 判断两次输入密码是否相同及当前用户是否存在，不同或用户已存在则返回注册页
    if upwd != upwd2 or count:
        return redirect(reverse('user:register'))
    # 加密
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd = s1.hexdigest()
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.uemai = uemail
    user.save()
    return redirect(reverse('user:login'))
    # return redirect('/user/login/')


# 登录
def login(request):
    context = {'title': '登录'}
    return render(request, 'df_user/login.html', context)


# 登录处理
def login_handle(request):
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    jizhu = request.POST.get('jizhu', 0)
    # 查询满足条件的对象，得到的是满足条件的对象列表
    user = UserInfo.objects.filter(uname=uname)
    # 判断拟登录用户是否存在，若存在判断密码是否正确
    if len(user) == 1:
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest() == user[0].upwd:
            # return redirect('/')
            url = request.COOKIES.get('url', '/')
            red = redirect(url)
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['id'] = user[0].id
            request.session['uname'] = uname
            return red
        else:
            return redirect(reverse('user:login'))
    else:
        return redirect(reverse('user:login'))


# 注销
def logout(request):
    # 清除所有session
    request.session.flush()
    return redirect('/')


# 用户中心信息
@login_decorator.login
def centerinfo(request):
    user = UserInfo.objects.get(uname=request.session['uname'])
    uname = user.uname
    uemail = user.uemai
    uaddr = user.uaddr
    context= {
        'title': '用户中心',
        'uname': uname,
        'uemail': uemail,
        'uaddr': uaddr,
    }
    return render(request, 'df_user/user_center_info.html', context)


# 用户订单信息
@login_decorator.login
def centerorder(request):
    context = {
        'title': '用户中心'
    }
    return render(request, 'df_user/user_center_order.html', context)


# 用户地址信息
@login_decorator.login
def centersite(request):
    context = {
        'title': '用户中心',
    }
    return render(request, 'df_user/user_center_site.html', context)


def centersite_handle(request):
    post = request.POST
    user = UserInfo.objects.get(uname=request.session['uname'])
    user.urecv = post.get('recv')
    user.uaddr = post.get('addr')
    user.upost = post.get('post')
    user.uphone = post.get('phone')
    user.save()
    context = {
        'user': user,
    }
    return render(request, 'df_user/user_center_site.html', context)
