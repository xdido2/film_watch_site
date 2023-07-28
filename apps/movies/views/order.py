from django.shortcuts import render

from apps.movies.forms.order import OrderForm


def order_view(request):
    forms = OrderForm
    if request.method == 'POST':
        form = forms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'films/main_content/order.html',
                          {'success': 'Ваша форма была отправлена, ждите ответ по email!'})
    else:
        return render(request, 'films/main_content/order.html')
