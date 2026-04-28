from django.contrib import admin
from .models import Wallet, Transaction, Payout

admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Payout)
