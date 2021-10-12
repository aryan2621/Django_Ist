from django.shortcuts import render
from .models import Shopping
# Create your views here.

from .forms import ShoppingForm, RawProductForm


def home(request):
    return render(request, 'home.html')


def product_create_view(request):
    my_form = RawProductForm(request.GET)
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Shopping.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "product/product_create.html", context)


# def product_create_view(request):
#     # if request.method == 'POST':
#     #     title = request.POST.get('title')


#     context = {}
#     return render(request, "product/product_create.html", context)


# def product_create_view(request):
#     form = ShoppingForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#     return render(request, "product/product_create.html", context)


def product_detail_view(request):
    obj = Shopping.objects.all()
    context = {
        'object': obj
    }

    return render(request, 'product/product_detail.html', context)
