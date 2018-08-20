from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # def __str__(self):
    #     return self.ttitle.encode("utf-8")

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to="df_goods")
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20, default="500g")
    gclick = models.IntegerField()
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcontent = HTMLField()
    gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE)
    # gadv = models.IntegerField(default=False)
    """
    on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
    on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
    on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
    on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
    # models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
    on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
    # models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
    on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
    on_delete=models.SET,         # 删除关联数据,
     a. 与之关联的值设置为指定值,设置：models.SET(值)
     b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)
    """
