from django.shortcuts import redirect, reverse
from django.core.mail import send_mail
from django.conf import settings


def purchased(request):
    subject = "This is your order from customer"
    message = "Order successful"
    email_form = settings.EMAIL_HOST_USER
    recipient_list = ['pranshu04.alwar@gmail.com', ]
    send_mail(subject, message, email_form, recipient_list)
    return redirect(reverse('all_products'))
