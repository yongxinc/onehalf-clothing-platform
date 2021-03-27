
# yourproject/catalogue/models.py

from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct
from datetime import date
from django.utils import timezone


class sellerApplicationRecord(models.Model):
    seller = models.CharField(max_length=20)
    item_id = models.CharField(max_length=20,default='')
    SIZE_CHOICES = (
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'))
    size = models.CharField(max_length=3,
                            choices=SIZE_CHOICES,
                            default='XXS')
    color = models.CharField(max_length=20)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)

class UNIQLOItem(models.Model):
    UpdateDate = models.DateTimeField('更新時間', auto_now=True)
    UNIQLOID = models.CharField(max_length=10)
    UNIQLOTitle = models.CharField(max_length=20)
    OriginalPrice = models.IntegerField(default=0)
    CLOTHES_TYPE_CHOICES = (
        ('outer-casual-outer', '外套類-休閒/機能/連帽外套'),
        ('outer-jacket', '外套類-風衣/大衣/西裝外套'),
        ('outer-ultralightdown', '外套類-特級極輕羽絨服'),
        ('outer-down', '外套類-羽絨外套'),
        ('outer-fleece', '外套類-刷毛系列'),
        ('bottoms-long-pants', '下身類-休閒長褲'),
        ('bottoms-jeans', '下身類-牛仔褲'),
        ('bottoms-long-pants', '下身類-休閒長褲'),
        ('bottoms-easy-and-gaucho', '下身類-九分褲'),
        ('bottoms-leggings', '下身類-緊身褲/內搭褲'),
        ('bottoms-widepants', '下身類-寬褲'),
        ('bottom-skirt', '下身類-裙子'),
        ('tops-short-sleeves-and-tank-top', '上衣類-短袖/背心'),
        ('tops-short-long-and-3-4sleeves-and-cardigan', '上衣類-長袖/七分袖'),
        ('tops-shirts-and-blouses', '上衣類-襯衫'),
        ('tops-sweat-collection', '上衣類-休閒/連帽上衣‧連帽外套'),
        ('tops-flannel', '上衣類-法蘭絨系列'),
        ('tops-knit', '上衣類-針織衫/毛衣/開襟外套'),
        ('tops-dresses', '上衣類-洋裝‧連身褲'),
        ('default', '尚未分類')
    )
    ClothesColorJSON = models.CharField(max_length=500)
    TitleImagesJSON = models.CharField(max_length=500)
    SubImagesJSON = models.CharField(max_length=2000)
    ClothesType = models.CharField(max_length=50,
                                   choices=CLOTHES_TYPE_CHOICES,
                                   default='default')

    Description = models.CharField(max_length=250)

    def __str__(self):
        return self.UNIQLOID + ' | ' + self.ClothesType + ' | ' + self.UNIQLOTitle

    class Meta:
        ordering = ['ClothesType', 'UNIQLOTitle']


class Product(AbstractProduct):
    SIZE_CHOICES = (
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'))

    Size = models.CharField(max_length=3,
                            choices=SIZE_CHOICES,
                            default='XXS')
    # ExtendTimes = models.IntegerField(default=0)
    # ExpireDate = models.DateField(default=date.today)
    # ArrivalDate = models.DateField(default=date.today)


# this must be at the last line
from oscar.apps.catalogue.models import *  # noqa isort:skip
