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


SIZE_CHOICES = (
    ('XXS', 'XXS'),
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'))


def _option_choices_field(option):
    return forms.ChoiceField(label=option.name, required=option.required, choices=SIZE_CHOICES)


def _option_text_field(option):
    return forms.CharField(label=option.name, required=option.required)


def _option_integer_field(option):
    return forms.IntegerField(label=option.name, required=option.required)


def _option_boolean_field(option):
    return forms.BooleanField(label=option.name, required=option.required)


def _option_float_field(option):
    return forms.FloatField(label=option.name, required=option.required)


def _option_date_field(option):
    return forms.DateField(label=option.name, required=option.required, widget=forms.widgets.DateInput)


class AddToBasketForm(AddToBasketForm):
    OPTION_FIELD_FACTORIES = {
        Option.TEXT: _option_text_field,
        Option.INTEGER: _option_integer_field,
        Option.BOOLEAN: _option_boolean_field,
        Option.FLOAT: _option_float_field,
        Option.DATE: _option_date_field,
        Option.CHOICES: _option_choices_field,
    }
    
class SimpleAddToBasketForm(SimpleAddToBasketMixin, AddToBasketForm):
    pass




# class SimpleAddToBasketForm(SimpleAddToBasketMixin, AddToBasketForm):
#     pass






# class Product(AbstractProduct):
#     SIZE_CHOICES = (
#         ('XXS', 'XXS'),
#         ('XS', 'XS'),
#         ('S', 'S'),
#         ('M', 'M'),
#         ('L', 'L'),
#         ('XL', 'XL'),
#         ('XXL', 'XXL'))

#     Size = models.CharField(max_length=3,
#                             choices=SIZE_CHOICES,
#                             default='XXS')
#     # ExtendTimes = models.IntegerField(default=0)
#     # ExpireDate = models.DateField(default=date.today)
#     # ArrivalDate = models.DateField(default=date.today)