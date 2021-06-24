from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


def index(request):
    form = Item.objects.all()
    template = loader.get_template('food_API/index.html')
    context = {'form' : form}
    return HttpResponse(template.render(context, request))                      # Same as render(request, 'food_API/index.html', context).

class IndexClassView(ListView):
    model = Item
    template_name = 'food_API/index.html'
    context_object_name = 'form'

def item(request):
    return HttpResponse('This is an item view')

def detail(request, item_id):
    form = Item.objects.get(pk = item_id)
    context = {'form' : form}
    return render(request, 'food_API/detail.html', context)

class FoodDetail(DetailView):                                                   # If switching from FBV to CBV, change "form" (passed in context in detail()) to "object" within the template, also change item_id to pk in urls
    model = Item
    template_name = 'food_API/detail.html'

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food_API:index')

    return render(request, 'food_API/item-form.html', {'form' : form})

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food_API/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def update_item(request, item_id):
    item = Item.objects.get(pk = item_id)
    form = ItemForm(request.POST or None, instance = item)

    if form.is_valid():
        form.save()
        return redirect('food_API:index')

    return render(request, 'food_API/item-form.html', {'form' : form, 'item' : item})

def delete_item(request, item_id):
    item = Item.objects.get(pk = item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food_API:index')

    return render(request, 'food_API/item-delete.html', {'item' : item})
