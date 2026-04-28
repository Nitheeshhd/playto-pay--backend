from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
import json
import razorpay

from .models import Wallet, Transaction, Payout


# 🔑 Razorpay Client
client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))


# ================= DASHBOARD =================
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# ================= CREDIT =================
@login_required
def credit_money(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            amount = int(data.get("amount", 0))

            if amount <= 0:
                return JsonResponse({"error": "Invalid amount"}, status=400)

            wallet, _ = Wallet.objects.get_or_create(user=request.user)

            wallet.balance += amount
            wallet.save()

            Transaction.objects.create(
                user=request.user,
                amount=amount,
                type="credit",
                status="success"
            )

            return JsonResponse({"message": "Money credited"})

        except Exception:
            return JsonResponse({"error": "Invalid request"}, status=400)

    return JsonResponse({"error": "Only POST allowed"}, status=405)


# ================= PAYOUT =================
@login_required
def request_payout(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            amount = int(data.get("amount", 0))
            account_number = data.get("account_number")
            ifsc = data.get("ifsc")
            name = data.get("name")

            # VALIDATION
            if amount <= 0:
                return JsonResponse({"error": "Invalid amount"}, status=400)

            if not account_number or len(account_number) < 8:
                return JsonResponse({"error": "Invalid account number"}, status=400)

            if not ifsc or len(ifsc) < 5:
                return JsonResponse({"error": "Invalid IFSC"}, status=400)

            if not name:
                return JsonResponse({"error": "Account holder name required"}, status=400)

            wallet = Wallet.objects.get(user=request.user)

            if wallet.balance < amount:
                return JsonResponse({"error": "Insufficient balance"}, status=400)

            wallet.balance -= amount
            wallet.held_balance += amount
            wallet.save()

            # SAVE PAYOUT
            Payout.objects.create(
                user=request.user,
                amount=amount,
                bank_account=account_number,
                status="processing"
            )

            # SAVE TRANSACTION
            Transaction.objects.create(
                user=request.user,
                amount=amount,
                type="debit",
                status="processing"
            )

            return JsonResponse({"message": "Payout requested"})

        except Exception:
            return JsonResponse({"error": "Invalid request"}, status=400)

    return JsonResponse({"error": "Only POST allowed"}, status=405)


# ================= BALANCE =================
@login_required
def get_balance(request):
    wallet, _ = Wallet.objects.get_or_create(user=request.user)

    return JsonResponse({
        "balance": wallet.balance,
        "held_balance": wallet.held_balance
    })


# ================= TRANSACTIONS =================
@login_required
def get_transactions(request):
    txns = Transaction.objects.filter(user=request.user).order_by('-id')

    return JsonResponse({
        "transactions": [
            {
                "type": t.type,
                "amount": t.amount,
                "status": t.status
            } for t in txns
        ]
    })


# ================= SIGNUP =================
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {"error": "User exists"})

        User.objects.create_user(username=username, password=password)
        return redirect('/login/')

    return render(request, 'signup.html')


# ================= RAZORPAY =================
@login_required
def create_order(request):
    try:
        amount = int(request.GET.get("amount", 0))

        if amount <= 0:
            return JsonResponse({"error": "Invalid amount"}, status=400)

        order = client.order.create({
            "amount": amount * 100,
            "currency": "INR",
            "payment_capture": "1"
        })

        return JsonResponse(order)

    except Exception:
        return JsonResponse({"error": "Order creation failed"}, status=400)


# ================= PROFILE =================
@login_required
def profile(request):
    return render(request, 'profile.html')


# ================= ADMIN =================
@staff_member_required
def admin_dashboard(request):
    total_users = User.objects.count()
    total_transactions = Transaction.objects.count()
    total_amount = sum(t.amount for t in Transaction.objects.all())

    return render(request, 'admin_dashboard.html', {
        "users": total_users,
        "transactions": total_transactions,
        "amount": total_amount
    })