from django.urls import path
from.import views  

urlpatterns = [
    path('hello/',views.say_hello,name="hello"),
    path('',views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.loginn,name='login'),
    path('insert/',views.insert,name="insert"),
    path('view/',views.view,name="view"),
    path('detailedview/<str:pk>',views.detailed_view,name="detailedview"),
    path("delete/<str:pk>",views.delete,name="delete"),
    path("update/<str:pk>",views.update,name="update"),
    path('login/',views.loginform,name="login"),
    path('welcomes/',views.welcome,name="welcome"),
    path('userlog/',views.userlog,name="userlog"),
    path('logoutuser/',views.logoutuser,name="logoutuser"),
    path('adminlog/',views.adminlog,name="adminlog"),
    path('alog/',views.alog,name="alog"),
]   