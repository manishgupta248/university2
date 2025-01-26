from django.urls import path
from . import views

urlpatterns = [
    path('user_detail/', views.user_detail, name='user_detail'),
    path('user/<int:user_id>/update/', views.user_update, name='user_update'),
]