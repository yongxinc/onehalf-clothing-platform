from django.db import models
from datetime import date
from datetime import datetime
from django.utils import timezone

class SellerBankAccount(models.Model):
    seller = models.ForeignKey(
        'partner.Partner',
        on_delete=models.CASCADE,
        )
   
    bank_code = models.CharField('bank_code 銀行代碼',default='', max_length=3)
    bank_name = models.CharField('bank_name 銀行名稱',default='', max_length=20)
    bank_account = models.CharField('bank_account 銀行帳號',default='', max_length=20)

    def __str__(self):
        return self.seller.name + ' | ' + self.bank_name + ' | ' + self.bank_name

    class Meta:
        ordering = ['seller', 'bank_name']


class SellerWithdrawRecord(models.Model):
    seller = models.ForeignKey('partner.Partner',on_delete=models.CASCADE,)
  
    submit_date = models.DateTimeField('儲存日期',default = timezone.now())
    transfered_date = models.DateTimeField('匯款完成日期', null=True, blank=True)

    STATUS_CHOICES = (
    ('default', '預設值'),
    ('submited', '申請已提交，處理中'),
    ('transfered', '已完成匯款'),)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default='default')

    def __str__(self):
        return self.seller.name + ' | ' + str(self.submit_date.date()) + ' | ' + self.status

    class Meta:
        ordering = ['seller', 'status', 'submit_date']
