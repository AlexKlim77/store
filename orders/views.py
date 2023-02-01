from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from common.views import TitleMixin
from orders.forms import OrderForm


class OrderCreateViews(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Store - Оформлення заказу'
    
    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateViews, self).form_valid(form)
