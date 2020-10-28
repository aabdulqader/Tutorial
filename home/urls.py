from django.urls import path
from .views import (
    home, 
    about, 
    contact, 
    register,
    logout_view,
    login_view,
    


)


app_name = 'home'




urlpatterns = [
    path('', home, name='home' ),
    path('about/', about, name='about' ),
    path('contact/', contact, name='contact' ),
    path('register/', register, name='register' ),
    path('logout/', logout_view, name='logout' ),
    path('login/', login_view, name='login' ),

]
