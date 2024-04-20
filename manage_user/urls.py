from django.urls import path
from . import views

app_name = 'manage_user'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add_user/', views.add_user, name='add_user'),
    path('logout/', views.logout_user, name='logout_user'),
]