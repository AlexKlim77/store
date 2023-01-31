from django.shortcuts import render
from django.views.generic.edit import  CreateView


class OrderCreateViews(CreateView):
    template_name = 'orders/order-create.html'

