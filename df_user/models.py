from django.db import models


class UserInfo(models.Model):
    uname = models.CharField(max_length=20, default='')
    upwd = models.CharField(max_length=40, default='')
    uemai = models.CharField(max_length=30, default='')
    urecv = models.CharField(max_length=20, default='')
    upost = models.CharField(max_length=6, default='')
    uphone = models.CharField(max_length=11, default='')
    uaddr = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.uname

