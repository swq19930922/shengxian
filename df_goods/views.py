from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# 首页
def index(request):
    # 获取所有分类
    types = TypeInfo.objects.all()
    # 按最新时间、最高人气各取四个商品展示
    type0 = types[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = types[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = types[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = types[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = types[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = types[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = types[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = types[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = types[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = types[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = types[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = types[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {
                'title': '首页',
                'type0': type0, 'type01': type01,
                'type1': type1, 'type11': type11,
                'type2': type2, 'type21': type21,
                'type3': type3, 'type31': type31,
                'type4': type4, 'type41': type41,
                'type5': type0, 'type51': type51,
               }
    return render(request, 'df_goods/index.html', context)


# 列表页
def goodslist(request, tid, cid, pid):  # 注意：tid，cid等均为字符串，注意转换
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    # newest = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    # 将最新的两个放在广告位
    newest = TypeInfo.objects.get(pk=int(tid)).goodsinfo_set.order_by('-id')[0:2]
    # 按照默认、价格、人气排序；两种方法均能实现，但第二种中要使用all方法，（对象）
    if cid == '1':
        glist = GoodsInfo.objects.filter(gtype_id=int(tid))
    elif cid == '2':
        glist = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('gprice')
    else:
        glist = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    # if cid=='1':
    #     glist = TypeInfo.objects.get(pk=int(tid)).goodsinfo_set.order_by('-id').all()
    # elif cid=='2':
    #     glist = TypeInfo.objects.get(pk=int(tid)).goodsinfo_set.order_by('gprice').all()
    # else:
    #     glist = TypeInfo.objects.get(pk=int(tid)).goodsinfo_set.order_by('-gclick').all()
    paginator = Paginator(glist,10)
    page = paginator.page(int(pid))

    context = {
                'title': '天天生鲜-商品列表',
                'typeinfo': typeinfo,
                'newest': newest,
                'glist': glist,
                'cid': cid,
                'paginator': paginator,
                'page': page,
            }
    return render(request, 'df_goods/list.html', context)


# 详细页
def detail(request, gid):
    goodsdetail = GoodsInfo.objects.get(pk=gid)
    typeinfo = TypeInfo.objects.get(pk=goodsdetail.gtype_id)
    newest = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    context = {
                'title': '商品详情',
                'goodsdetail': goodsdetail,
                'typeinfo': typeinfo,
                'newest': newest,
            }
    return render(request, 'df_goods/detail.html', context)
