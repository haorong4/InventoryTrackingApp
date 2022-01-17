from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
import csv

def index(request):
    items = Item.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()

    context = {
        'items' : items,
        'form' : form,
    }   
    return render(request, 'dashboard/index.html', context)

def item_edit(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            print("edit successful")
            form.save()
            return redirect('index')
    else:
        form = ItemForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/edit.html', context)

def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    context = {
        'item': item
    }
    return render(request, 'dashboard/delete.html', context)


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="items.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'quantity'])

    users = Item.objects.all().values_list('name', 'quantity')
    for user in users:
        writer.writerow(user)

    return response
