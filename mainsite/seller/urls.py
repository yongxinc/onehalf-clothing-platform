from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.apps import apps
from django.conf.urls.static import static
from mainsite.seller.views import (
    SellerListView, SellerCreateView, SellerDeleteView, 
    SellerUpdateRevenueView, SellerUpdateWithdrawView, SellerApplicationListView,SellerUpdateApplicationView,
    SellerApplicationDeleteView)
from mainsite import views

app_name = 'seller'
urlpatterns = [
url(r'^$',SellerListView.as_view(),name='seller-list'),
path('create', SellerCreateView.as_view(), name='seller-create'),
path('update-withdraw/<int:pk>', SellerUpdateWithdrawView.as_view(), name='seller-update-withdraw'), #主鍵參數一定要命名為pk，這也是在撰寫Django類別導向的檢視(Class-based Views)規範，否則會出現錯誤。
path('update-revenue/<int:pk>', SellerUpdateRevenueView.as_view(), name='seller-update-revenue'), #主鍵參數一定要命名為pk，這也是在撰寫Django類別導向的檢視(Class-based Views)規範，否則會出現錯誤。
path('delete/<int:pk>', SellerDeleteView.as_view(), name='seller-delete'),

path('application-list', SellerApplicationListView.as_view(), name='seller-application-list'),
path('update-application/<int:pk>', SellerUpdateApplicationView.as_view(), name='seller-update-application'),
path('delete-applition/<int:pk>', SellerApplicationDeleteView.as_view(), name='seller-delete-application'),

]
