from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from webpush import send_group_notification, send_user_notification

def index_view(request):
    # webpush = {"group": "pop" } # The group_name should be the name you would define.

    return render(request, 'notif.html', )

def send_view(request):
    # webpush = {"group": "pop" } # The group_name should be the name you would define.

    payload = {"head": "Welcome!", "body": "Hello World"}

    send_user_notification(user=User.objects.first(), payload=payload, ttl=1000)
    return render(request, 'notif.html', )