from django.contrib import admin
from trade.models import Commodity, Trade, Request
# Register your models here.

admin.site.register(Commodity)
admin.site.register(Trade)
admin.site.register(Request)
