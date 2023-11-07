from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),

    path('userdetails/',views.userdetails,name="userdetails"),
    path('editprofile/',views.edit_profile,name="editprofile"),
    path("", views.index, name="index"),
    path('chatroom/<str:pk>/',views.chatroom,name="chatroom")#very imp 
]
 