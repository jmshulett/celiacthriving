from django.urls import path
from . import views
app_name = 'tips'
urlpatterns = [
    path('', views.tips_list, name='tips_list'),
    path('<slug:tips_slug>/', views.tips_list,
         name='tips_list_by_category'),
    path('<int:id>/<slug:slug>/', views.tips_detail,
         name='tips_detail'),
]