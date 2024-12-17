from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('reflections/', views.reflections_index, name='reflections-index'),
    path('reflections/<int:reflection_id>/', views.reflection_detail, name='reflection-detail'),
    path('reflections/create', views.ReflectionCreate.as_view(), name='reflections-create'),
    path('reflections/<int:pk>/update/', views.ReflectionUpdate.as_view(), name='reflection-update'),
    path('reflections/<int:pk>/delete/', views.ReflectionDelete.as_view(), name='reflection-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('reflections/<int:reflection_id>/add_response/', views.add_response, name='add-response'),
    # path('friends/', views.index_friends, name='index-friends'),
    # path('accept_request/<int:request_id>/', views.accept_request, name='accept_request'),
    # path('reject_request/<int:request_id>/', views.reject_request, name='reject_request'),
]