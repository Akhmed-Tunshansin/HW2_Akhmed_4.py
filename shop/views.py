from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Purchase


def greetings(request):
    return HttpResponse("Добро пожаловать в наш магазин!")


def list_item(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'list_item.html', context)


def detail_item(request, item_id):
    item = Purchase.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, 'detail_item.html', context)