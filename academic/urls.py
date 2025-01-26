from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list_create_update, name='course_list_create_update'),
    path('courses/<int:pk>/update/', views.course_list_create_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
]
