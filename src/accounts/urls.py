from django.urls import path

from .views import *


urlpatterns = [
    path('', AccountView.as_view(), name='account'),
    # path('admin/', ),
    path('login/', LoginView.as_view(), name='login'),
    #path('register/', RegisterView.as_view(), name='register'),
    path('register/', registerPage, name='register'),

]