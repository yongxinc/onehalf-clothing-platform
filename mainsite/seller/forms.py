from django import forms
from mainsite.order.models import SellerRevenue
from .models import SellerBankAccount, SellerWithdrawRecord


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