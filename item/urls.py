from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('jitems/', views.Item_list),
    path('jitems/<int:id>', views.item_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
