# from oscar.apps.basket.abstract_models import AbstractBasket
from oscar.apps.basket.forms import AddToBasketForm, SimpleAddToBasketForm, SimpleAddToBasketMixin
from django import forms
from django.conf import settings
from django.db.models import Sum
from django.forms.utils import ErrorDict
from django.utils.translation import gettext_lazy as _

from oscar.core.loading import get_model
from oscar.forms import widgets

Line = get_model('basket', 'line')
Basket = get_model('basket', 'basket')
Option = get_model('catalogue', 'Option')
Product = get_model('catalogue', 'product')
ProductAttribute = get_model('catalogue', 'ProductAttribute')
ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')
UNIQLOItem = get_model('catalogue','UNIQLOItem')

def _option_text_field(option, product):
        return forms.CharField(label=option.name, required=option.required)

def _option_integer_field(option, product):
        return forms.IntegerField(label=option.name, required=option.required)

def _option_boolean_field(option, product):
        return forms.BooleanField(label=option.name, required=option.required)

def _option_float_field(option, product):
        return forms.FloatField(label=option.name, required=option.required)

def _option_date_field(option, product):
        return forms.DateField(label=option.name, required=option.required, widget=forms.widgets.DateInput)
    
def trimAttribueValue(attr):
    tmp = attr.replace('尺寸: ','')
    size_list = tmp.split(', ')

    for i in range(0, len(size_list)):
        size_list[i] = (size_list[i],size_list[i])
    # print('DIY',tuple(size_list))
    size_tuple = tuple(size_list)
    return size_tuple

def _option_choices_field(option, product):
    SIZE_CHOICES = (
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'))
    print('true',SIZE_CHOICES)
    attribute = ProductAttribute.objects.filter(name='尺寸')
        # target_product = Product.objects.filter(upc='12345')
    product_attribute_value = ProductAttributeValue.objects.filter(attribute=attribute[0],product=product)
    size_tuple = trimAttribueValue(str(product_attribute_value[0]))

    # print(str(product_attribute_value[0]))
    
        # item = ProductAttributeValue.objects.filter(attribute=attribute[0],product=target_product)

        # for value in item:
        #     print(value)
    return forms.ChoiceField(label=option.name, required=option.required, choices=size_tuple)

class AddToBasketForm(AddToBasketForm):
    
    OPTION_FIELD_FACTORIES = {
            Option.TEXT: _option_text_field,
            Option.INTEGER: _option_integer_field,
            Option.BOOLEAN: _option_boolean_field,
            Option.FLOAT: _option_float_field,
            Option.DATE: _option_date_field,
            Option.CHOICES: _option_choices_field,
        }

    def _add_option_field(self, product, option):
        """
        Creates the appropriate form field for the product option.

        This is designed to be overridden so that specific widgets can be used
        for certain types of options.
        """
        target_product = self.product
        product_title = target_product.get_title
        product_upc = target_product.upc

        option_field = self.OPTION_FIELD_FACTORIES.get(option.type, Option.TEXT) (option, product)
        # test
        # print('option.type',option.type) #choices
        # print('option',option) #尺寸
        # print('Option',Option) #<class 'mainsite.catalogue.models.Option'>
        # print('_add_option_field',type(option_field)) #<class 'django.forms.fields.ChoiceField'>

        # print the product info in this showing page
        # print(product_title, product_upc)

        self.fields[option.code] = option_field
    
class SimpleAddToBasketForm(SimpleAddToBasketMixin, AddToBasketForm):
    pass
