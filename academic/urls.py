from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list_create_update, name='course_list_create_update'),
    path('courses/<int:pk>/update/', views.course_list_create_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('courses/import/', views.course_import, name='course_import'),
    path('courses/export/',views.course_export, name='course_export'),
    path('course-detail/<int:pk>/', views.course_detail, name='course_detail'),
]
