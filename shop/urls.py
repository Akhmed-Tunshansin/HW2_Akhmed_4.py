from django.urls import path
from . import views



urlpatterns = [
    path('greetings', views.greetings),
    path('', views.list_item, name='list_item'),
    path('<int:item_id>/', views.detail_item, name='detail_item'),
]