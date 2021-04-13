# from oscar.apps.basket.abstract_models import AbstractBasket
from oscar.apps.basket.forms import AddToBasketForm, SimpleAddToBasketForm, SimpleAddToBasketMixin
from django import forms
from django.conf import settings
from django.db.models import Sum
from django.forms.utils import ErrorDict
from django.utils.translation import gettext_lazy as _

from oscar.core.loading import get_model
from oscar.forms import widgets
import json

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
    
def trimAttribueValue(attr, option_name):
    if option_name == '尺寸':
        tmp = attr.replace('尺寸: ','')
        size_list = tmp.split(', ')

        for i in range(0, len(size_list)):
            size_list[i] = (size_list[i],size_list[i])
        size_tuple = tuple(size_list)
        return size_tuple
    elif option_name == '顏色':
        tmp = attr.replace('顏色: ','')
        color_list = tmp.split(', ')

        for i in range(0, len(color_list)):
            color_list[i] = (color_list[i],color_list[i])
        color_tuple = tuple(color_list)
        return color_tuple

def getColorTupleFromJSON(jsonSoup):
    # print('getColorTupleFromJSON')
    color_dict = json.loads(jsonSoup)
    color_tuple = turnDictToTuple(color_dict)
    return color_tuple

def turnDictToTuple(someDict):
    # print('turnDictToTuple')
    color_view = someDict.items()
    color_list = list(color_view)
    color_tuple = tuple(color_list)
    return color_tuple

def _option_choices_field(option, product):
    if option.name == '尺寸':
        size_attribute = ProductAttribute.objects.filter(name='尺寸')
        size_product_attribute_value = ProductAttributeValue.objects.filter(attribute=size_attribute[0],product=product)
        size_tuple = trimAttribueValue(str(size_product_attribute_value[0]),'尺寸')
        print('size option generated')
        return forms.ChoiceField(label=option.name, required=option.required, choices=size_tuple)
    elif option.name == '顏色':
        color_attribute = ProductAttribute.objects.filter(name='顏色')
        color_product_attribute_value = ProductAttributeValue.objects.filter(attribute=color_attribute[0],product=product)
        color_tuple = trimAttribueValue(str(color_product_attribute_value[0]),'顏色')
        print('color option generated')
        return forms.ChoiceField(label=option.name, required=option.required, choices=color_tuple)
    # start of test_area
    # print(str(product_attribute_value[0]))
    
        # item = ProductAttributeValue.objects.filter(attribute=attribute[0],product=target_product)

        # for value in item:
        #     print(value)
    # end of test_area
    

class AddToBasketForm(AddToBasketForm):
    
    OPTION_FIELD_FACTORIES = {
            Option.TEXT: _option_text_field,
            Option.INTEGER: _option_integer_field,
            Option.BOOLEAN: _option_boolean_field,
            Option.FLOAT: _option_float_field,
            Option.DATE: _option_date_field,
            Option.CHOICES: _option_choices_field,
        }
    quantity = forms.IntegerField(initial=1, min_value=1, label=_('Quantity'))
    def _add_option_field(self, product, option):
        """
        Creates the appropriate form field for the product option.

        This is designed to be overridden so that specific widgets can be used
        for certain types of options.
        """
       
        option_field = self.OPTION_FIELD_FACTORIES.get(option.type, Option.TEXT) (option, product)

        # start of test_area
        # print('option.type',option.type) #choices
        # print('option',option) #尺寸
        # print('Option',Option) #<class 'mainsite.catalogue.models.Option'>
        # print('_add_option_field',type(option_field)) #<class 'django.forms.fields.ChoiceField'>

        # print the product info in this showing page
        # print(product_title, product_upc)
        # end of test_area
        self.fields[option.code] = option_field
    
class SimpleAddToBasketForm(SimpleAddToBasketMixin, AddToBasketForm):
    pass
