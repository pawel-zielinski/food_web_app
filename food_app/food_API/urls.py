from django.urls import path
from . import views


app_name = 'food_API'

urlpatterns = [
    path('', views.IndexClassView.as_view(), name = 'index'),
    path('item/', views.item, name = 'item'),
    path('<int:pk>/', views.FoodDetail.as_view(), name = 'detail'),              # '<int:item_id>/' if function based view
    path('add/', views.CreateItem.as_view(), name = 'create_item'),
    path('update/<int:item_id>/', views.update_item, name = 'update_item'),
    path('delete/<int:item_id>/', views.delete_item, name = 'delete_item'),
]
