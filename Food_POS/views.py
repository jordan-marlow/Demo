from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView

# Create your views here.

from .models import Item,Ingredient,Transaction

class ItemCreateView(CreateView):
    model = Item
    template_name = 'item_create.html'
    success_url = 'success'
    fields = "__all__"

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = 'ingredient_create.html'
    success_url = 'success'
    fields = "__all__"

class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'transaction_create.html'
    success_url = 'success'

class ItemDeleteView(CreateView):
    model = Item
    template_name = 'item_delete.html'
    success_url = 'success'

class IngredientDeleteView(CreateView):
    model = Ingredient
    template_name = 'ingredient_delete.html'
    success_url = 'success'

class TransactionDeleteView(CreateView):
    model = Transaction
    template_name = 'transaction_delete.html'
    success_url = 'success'

