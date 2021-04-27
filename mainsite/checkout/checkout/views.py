from oscar.apps.checkout import views as AbstractCheckoutView
from mainsite.order import models as order
from oscar.apps.partner import models as oscar_partner
from django.contrib import auth

class ThankYouView(AbstractCheckoutView.ThankYouView):
    """
    Displays the 'thank you' page which summarises the order just submitted.
    """
    template_name = 'oscar/checkout/thank_you.html'
    # context_object_name = 'order'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object is None:
            return redirect(settings.OSCAR_HOMEPAGE)
        context = self.get_context_data(object=self.object)

        #新增更新 revenue資料
        username= request.user
        user = auth.models.User(username=username)
        orders = order.Order.objects.filter(user=user)
        partner = oscar_partner.Partner.objects.get(name=username)
        orders_line = order.Line.objects.filter(partner=partner)


        try:#看看sellerRevenue是不是有這位賣家的資料
            sellerRevenue = order.SellerRevenue.objects.get(seller=partner)
            #更新資料
        except:#如果沒有，就新增
            print('不存在',partner,'所以新增一筆SellerRevenue')
            sellerRevenue = order.SellerRevenue(seller=partner,balance=0,withdrawn=0)
            sellerRevenue.save()
            # sellerRevenue = oscar.SellerRevenue.objects.get(seller = partner)


        totalRevenue = 0 #個人銷售總額 要另外計算的
        withdrawn = sellerRevenue.withdrawn

        # 計算個人銷售總額(totalRevenue)
        for line in orders_line:
            totalRevenue += line.line_price_incl_tax
            # print(line.line_price_incl_tax)

        #計算餘額
        balance = totalRevenue - withdrawn

        #存回去SellerRevenue
        sellerRevenue.balance = balance
        sellerRevenue.withdrawn = withdrawn
        sellerRevenue.totalRevenue = totalRevenue
        sellerRevenue.save()

        return self.render_to_response(context)

    # def get_object(self, queryset=None):
    #     # We allow superusers to force an order thank-you page for testing
    #     order = None
    #     if self.request.user.is_superuser:
    #         kwargs = {}
    #         if 'order_number' in self.request.GET:
    #             kwargs['number'] = self.request.GET['order_number']
    #         elif 'order_id' in self.request.GET:
    #             kwargs['id'] = self.request.GET['order_id']
    #         order = Order._default_manager.filter(**kwargs).first()

    #     if not order:
    #         if 'checkout_order_id' in self.request.session:
    #             order = Order._default_manager.filter(
    #                 pk=self.request.session['checkout_order_id']).first()
    #     return order

    # def get_context_data(self, *args, **kwargs):
    #     ctx = super().get_context_data(*args, **kwargs)
    #     # Remember whether this view has been loaded.
    #     # Only send tracking information on the first load.
    #     key = 'order_{}_thankyou_viewed'.format(ctx['order'].pk)
    #     if not self.request.session.get(key, False):
    #         self.request.session[key] = True
    #         ctx['send_analytics_event'] = True
    #     else:
    #         ctx['send_analytics_event'] = False

    #     return ctx
