from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns=[
    url(r"^accounts/", include("django.contrib.auth.urls")),
    path("",views.dashboard,name="dashboard"),
    path("register",views.register,name="register")
]