from oscar.apps.basket.models import *  # noqa isort:skip
from oscar.apps.basket.abstract_models import AbstractBasket
from django.db import models

# class Basket(AbstractBasket):
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