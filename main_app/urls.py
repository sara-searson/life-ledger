from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reflections/', views.reflections_index, name='reflections-index'),
    path('reflections/<int:reflection_id>/', views.reflection_detail, name='reflection-detail'),
    path('reflections/create', views.ReflectionCreate.as_view(), name='reflections-create'),
    path('reflections/<int:pk>/update/', views.ReflectionUpdate.as_view(), name='reflection-update'),
    path('reflections/<int:pk>/delete', views.ReflectionDelete.as_view(), name='reflection-delete'),
]