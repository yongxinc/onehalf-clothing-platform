from django.db import models
from oscar.apps.order.models import *  # noqa isort:skip
from oscar.apps.order.abstract_models import AbstractOrder

class SellerRevenue(models.Model):
    seller = models.ForeignKey(
        'partner.Partner',
        on_delete=models.CASCADE,
       )
    totalRevenue = models.IntegerField('totalRevenue 個人銷售總額',default=0)
    balance = models.IntegerField('balance 餘額',default=0)
    withdrawn = models.IntegerField('withdrawn 已提領',default=0)

    def __str__(self):
        return self.seller.name + ' | ' + 'totalRevenue $' + str(self.totalRevenue)

    class Meta:
        ordering = ['seller', 'totalRevenue']
    