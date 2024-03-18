from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('route1/', views.route1, name='route1'),
    path('route2/', views.route2, name='route2'),

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name="login"),
    path('accounts/register/', views.register, name="register"),
    path('accounts/logout/', views.logout_view, name="logout"),
]
