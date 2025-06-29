from django.shortcuts import render
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment

class InitiatePaymentView(APIView):
    def post(self, request):
        data = request.data
        payload = {
            "amount": data['amount'],
            "currency": "ETB",
            "email": data['email'],
            "first_name": data.get('first_name', 'User'),
            "last_name": data.get('last_name', 'User'),
            "tx_ref": data['booking_reference'],
            "callback_url": "https://yourdomain.com/callback/",
            "return_url": "https://yourdomain.com/return/",
            "customization[title]": "Booking Payment",
        }

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
        }

        response = requests.post("https://api.chapa.co/v1/transaction/initialize", json=payload, headers=headers)

        if response.status_code == 200:
            res_data = response.json()
            Payment.objects.create(
                booking_reference=data['booking_reference'],
                transaction_id=res_data['data']['tx_ref'],
                amount=data['amount']
            )
            return Response({"payment_url": res_data['data']['checkout_url']})
        return Response({"error": "Failed to initiate payment"}, status=status.HTTP_400_BAD_REQUEST)


class VerifyPaymentView(APIView):
    def get(self, request, tx_ref):
        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
        }
        url = f"https://api.chapa.co/v1/transaction/verify/{tx_ref}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            res_data = response.json()
            status_from_api = res_data['data']['status']
            payment = Payment.objects.filter(transaction_id=tx_ref).first()
            if payment:
                payment.status = status_from_api
                payment.save()
            return Response({"status": status_from_api})
        return Response({"error": "Failed to verify payment"}, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
