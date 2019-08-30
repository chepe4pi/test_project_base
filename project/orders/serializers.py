from rest_framework.serializers import ModelSerializer

from orders.models import SalesOrder


class SalesOrderSerializer(ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['amount', 'description']
