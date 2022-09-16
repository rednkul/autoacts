from django.urls import path
from . import views

app_name = 'acts'

urlpatterns = [
    path('types/<int:pk>/', views.TypeDetailView.as_view(), name='type_detail'),
    path('types/create/', views.TypeCreateView.as_view(), name='type_create'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('acts/create/', views.ActCreateView.as_view(), name='act_create'),
    path('materials/create/', views.MaterialCreateView.as_view(), name='material_create'),

]