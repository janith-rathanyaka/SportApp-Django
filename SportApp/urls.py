
from django.urls import path
from .views import Sport,Home,Contact

urlpatterns = [
     path('',Home,name='home'),
     path('sport/',Sport,name='sport'),
     path('contact/',Contact,name='contact'),

]
