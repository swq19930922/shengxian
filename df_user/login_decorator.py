from django.shortcuts import redirect
from django.core.urlresolvers import reverse


# 如果未登录就转至登录界面
def login(func):
    def login_fun(request, *args, **kwargs):
        if request.session.has_key('uname'):      # 判断session中是否有user_id,如果没有,则未登录
            return func(request, *args, **kwargs)
        else:
            red = redirect(reverse('user:login'))
            red.set_cookie('url', request.get_full_path())   # 把路径放在cookie中,名字为url
            return red
    return login_fun
