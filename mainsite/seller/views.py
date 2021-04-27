# from django.shortcuts import render
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import SellerRevenueForm, SellerWithdrawRecordForm, ApplicationRecordForm

# from oscar.apps.partner.models import StockRecord
from mainsite.order.models import SellerRevenue #之後移到seller裡面
from mainsite.catalogue.models import Application_Records #之後移到seller裡面
from .models import SellerWithdrawRecord
from django.http import HttpResponse


# class SellerListView(TemplateView):
class SellerListView(ListView):
    model = SellerWithdrawRecord
    template_name= 'oscar/seller/seller_list.html'

    # 要傳遞的資料
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SellerWithdrawRecordForm()  #資料模型表單
        return context

class SellerCreateView(CreateView):
    template_name= 'oscar/seller/seller_create.html'
    model = SellerWithdrawRecord
    form_class = SellerWithdrawRecordForm # 使用的表單類別
    success_url = '/dashboard/seller/'  # 儲存成功後要導向的網址

class SellerUpdateWithdrawView(UpdateView):
    model =  SellerWithdrawRecord
    form_class = SellerWithdrawRecordForm
    template_name = 'oscar/seller/seller_update_withdraw.html'  # 修改樣板
    success_url = '/dashboard/seller/'  # 儲存成功後要導向的網址


class SellerUpdateRevenueView(UpdateView):
    model =  SellerRevenue
    form_class = SellerRevenueForm
    template_name = 'oscar/seller/seller_update_revenue.html'  # 修改樣板
    success_url = '/dashboard/seller/'  # 儲存成功後要導向的網址

class SellerDeleteView(DeleteView):
    model = SellerWithdrawRecord
    template_name = 'oscar/seller/seller_delete.html'  # 刪除樣板
    success_url = '/dashboard/seller/'  # 刪除成功後要導向的網址



class SellerApplicationListView(ListView):
    model = Application_Records
    template_name= 'oscar/seller/application/seller_application_list.html'

    # 要傳遞的資料
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ApplicationRecordForm()  #資料模型表單
        return context

class SellerUpdateApplicationView(UpdateView):
    model =  Application_Records
    form_class = ApplicationRecordForm
    template_name = 'oscar/seller/application/seller_application_update.html'  # 修改樣板
    success_url = '/dashboard/seller/application-list'  # 儲存成功後要導向的網址
    

class SellerApplicationDeleteView(DeleteView):
    model = Application_Records
    target='上架申請紀錄'
    template_name = 'oscar/seller/application/seller_application_delete.html'  # 刪除樣板
    success_url = '/dashboard/seller/application-list'  # 儲存成功後要導向的網址
