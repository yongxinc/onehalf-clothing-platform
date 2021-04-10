# yourproject/catalogue/models.py

from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractOption, AbstractProductAttributeValue
from datetime import date
from django.utils import timezone
from django.utils.translation import gettext as _
from oscar.models.fields import AutoSlugField, NullCharField
from oscar.core.decorators import deprecated

SIZE_CHOICES = (
    ('XXS', 'XXS'),
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),)

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

    Size = models.CharField(max_length=3,
                            choices=SIZE_CHOICES,
                            default='XXS')
   
    # ExtendTimes = models.IntegerField(default=0)
    # ExpireDate = models.DateField(default=date.today)
    # ArrivalDate = models.DateField(default=date.today)

# class ProductAttributeValue(AbstractProductAttributeValue):
    

class Option(AbstractOption):

     # Option types
    TEXT = "text"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"
    CHOICES = "choices"

    TYPE_CHOICES = (
        (TEXT, _("Text")),
        (INTEGER, _("Integer")),
        (BOOLEAN, _("True / False")),
        (FLOAT, _("Float")),
        (DATE, _("Date")),
        (CHOICES,_("Choices")),
    )
   
    type = models.CharField(_("Type"), max_length=255, default=TEXT, choices=TYPE_CHOICES)
    
class Application_Records(models.Model):
    username = models.CharField(max_length=30)
    status = models.CharField(max_length=50)
    UNIQLOID = models.CharField(max_length=20,default='')
    title = models.CharField(max_length=50,default='')
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    wishing_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.username + ' | ' +self.UNIQLOID +  ' | ' +self.title +  ' | '+ self.status 

    class Meta:
        ordering = ['username', 'UNIQLOID']

#顏色的資料庫
class color(models.Model):
    color_code =  models.CharField(max_length=10)
    color_name =  models.CharField(max_length=30)
    color_name_ch = models.CharField(max_length=10, default='')
    # color_chip_url = models.URLField(default='')


    def __str__(self):
        return self.color_code + ' | ' +self.color_name +  ' | ' +self.color_name_ch
    class Meta:
        ordering = ['color_code']

class size(models.Model):
    size =  models.CharField(max_length=10)

# this must be at the last line
from oscar.apps.catalogue.models import *  # noqa isort:skip
