from django.contrib import admin
from .models import *


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tname']
    list_per_page = 10


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gname', 'gtype']
    list_per_page = 10


admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
