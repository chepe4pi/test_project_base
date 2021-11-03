from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import SalesOrderSerializer


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


class OrderViewSet(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer


def main_app_page(request):
    return render(request, 'main_app_page.html')
