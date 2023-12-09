
from django.urls import path
from . import views as v



urlpatterns = [
    path('signup/',v.sign_up, name="signup"),
    path('login/',v.log_in, name="login"),
    path('logout/',v.log_out, name="logout")
]