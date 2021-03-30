from django import forms

class SellerApplicationForm(forms.Form):
    seller = forms.HiddenInput()
    item_id = forms.CharField(label='商品序號',max_length=20)
    color = forms.CharField(label='商品顏色',max_length=20)
    SIZE_CHOICES = (
        ('DEFAULT', '----'),
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'))

    size = forms.ChoiceField(label='尺寸',choices=SIZE_CHOICES,initial='default')
   
    quantity = forms.IntegerField(max_value=99)
    status = forms.HiddenInput() #initial='已送出申請，平台上未收到商品'
    wishing_price = forms.IntegerField(max_value=3000)


