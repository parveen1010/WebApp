from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
   	path('add_user/', views.add, name="add_user" ),
   	path('delete_user/<str:pk>', views.deleteUser, name="delete_user"),
   	path('update_user/<str:pk>', views.updateUser, name="update_user"),

]