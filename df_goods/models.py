from django.db import models
from tinymce.models import HTMLField


# 商品种类
class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.tname


# 商品
class GoodsInfo(models.Model):
    gname = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='media')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=10)
    gclick = models.IntegerField()
    gprofile = models.CharField(max_length=200)
    gdetail = HTMLField()
    gcomment = models.CharField(max_length=800, default='')
    gleft = models.IntegerField()
    gtype = models.ForeignKey(TypeInfo)

    def __str__(self):
        return self.gname

