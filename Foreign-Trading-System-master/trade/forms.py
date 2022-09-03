from django import forms
from .models import Commodity, Request

class CommodityForm(forms.ModelForm):
    class Meta:
        model = Commodity
        fields = [
            'commodityName',
            # 'exporterName',
            'price',
            'quantityAvailable',
            'description'
        ]

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'commodityName',
            'exporterName',
            'quantityRequested'
        ]
