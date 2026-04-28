from django.db import models
from django.contrib.auth.models import User


# =========================
# 💰 WALLET MODEL
# =========================
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    held_balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Wallet"


# =========================
# 📜 TRANSACTION MODEL
# =========================
class Transaction(models.Model):

    TRANSACTION_TYPE = (
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    )

    STATUS_CHOICES = (
        ('success', 'Success'),
        ('processing', 'Processing'),
        ('failed', 'Failed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.type} - ₹{self.amount}"


# =========================
# 🏦 PAYOUT MODEL
# =========================
class Payout(models.Model):

    STATUS_CHOICES = (
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    bank_account = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - ₹{self.amount} - {self.status}"