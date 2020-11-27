from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('postad', views.postad, name='post'),
    path('dashboard', views.dashboard, name='dashboard'),
 	path('delete/<int:list_id>', views.delete, name='delete'),
 	path('delete_list/<int:list_id>', views.delete_list, name='delete_list'),
 	path('edit_profile/<int:user_id>', views.edit_profile, name='edit_profile'),
 	path('edit_listing/<int:list_id>', views.edit_listing, name='edit_listing')
       
]

