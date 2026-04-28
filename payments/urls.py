from django.urls import path
from .views import (
    dashboard,
    credit_money,
    request_payout,
    get_balance,
    get_transactions,
    signup,
    create_order,
    profile,
)


urlpatterns = [
    path('dashboard/', dashboard),
    path('credit/', credit_money),
    path('payout/', request_payout),
    path('balance/', get_balance),
    path('transactions/', get_transactions),
    path('signup/', signup),
    path('create-order/', create_order),
    path('profile/', profile),
]