from django import forms
from mainsite.order.models import SellerRevenue
from .models import SellerBankAccount, SellerWithdrawRecord
from mainsite.catalogue.models import Application_Records #之後移到seller裡面


class SellerRevenueForm(forms.ModelForm):

    class Meta:
        model = SellerRevenue
        fields = '__all__'
        labels = {
            'seller': '賣家',
        }

class SellerWithdrawRecordForm(forms.ModelForm):

    class Meta:
        model = SellerWithdrawRecord
        fields = '__all__'
        labels = {
            'seller': '賣家',
        }


# class SellerBankingForm(forms.ModelForm):

#     class Meta:
#         model = SellerBankAccount
#         # fields = 'bank_code', 'bank_name','bank_account'
#         fields = '__all__'
#         labels = {
#             'bank_code': '銀行代碼',
#             'bank_name':'銀行及分行名稱',
#             'bank_account':'帳號',

#         }
# 
# Application_Records

class ApplicationRecordForm(forms.ModelForm):

    class Meta:
        model = Application_Records
        fields = '__all__'
        labels = {
            'username': '使用者名稱',
        }
        