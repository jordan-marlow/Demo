from django.urls import path

from .views import IngredientCreateView,IngredientDeleteView

urlpatterns = [
    path('createingredient/',IngredientCreateView.as_view(),name="create_ingredient"),
    path('deleteingredient/',IngredientDeleteView.as_view(),name="delete_ingredient"),
]