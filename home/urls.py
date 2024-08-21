from django.urls import path
from home.views import home, aboutus, parms, home_template, home_redirect


urlpatterns = [
    path('', home, name='home-url'),
    path('aboutus/<str:data>', aboutus, name='aboutus-url'),
    path('test-parms', parms, name='aboutus-url'),
    path('dynamic', home_template, name='dynamic-url'),
    path('redirect', home_redirect, name='redirect-url'),
]