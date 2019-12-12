from django.shortcuts import render
from api.forms.order_form import OrderForm


def order(request):
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form': form
        }
        return render(request, 'order.html', context)
