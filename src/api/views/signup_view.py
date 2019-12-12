from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse

from api.forms.signup_form import SignupForm
from api.models.user_models import User
from api.models.seller_models import Seller
from api.models.buyer_models import Buyers


def sign_up(request):
    if request.method == "GET":
        form = SignupForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'signup.html', context)

    elif request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                username=form.cleaned_data["username"],
                contact_no=form.cleaned_data["contact_no"],
                email=form.cleaned_data["username"],
                gender=form.cleaned_data["gender"],
                dob=form.cleaned_data["dob"],
                image=form.cleaned_data["image"],
                is_active=True
            )
            password = form.cleaned_data["password"]
            user.set_password(password)
            if request.POST.get("signup_choice_dropdown"):
                seller = Seller.objects.create(
                    user=user,
                    is_verified=False
                )
                seller.save()
            else:
                buyer = Buyers.objects.create(
                    user=user,
                )
                buyer.save()
            user.save()

        else:
            for key, value in form.errors.items():
                tmp = {'key': key, 'error': value.as_text()}
                print(tmp)
    return redirect("product/")

    """
                string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                password = "".join(random.sample(string, 8))
                user.set_password(password)
                user.save()
    """
