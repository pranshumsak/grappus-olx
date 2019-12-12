from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from api.forms.login_form import LoginForm
from api.models.buyer_models import Buyers
from api.models.seller_models import Seller


def ulogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        choice = request.POST.get('choice')
        print(choice)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if Buyers.objects.filter(user=user).exists():
                    login(request, user)
                    return redirect("product")
                elif Seller.objects.filter(user=user).exists():
                    login(request, user)
                    return redirect("product")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password:{}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:

        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'login.html', context)
