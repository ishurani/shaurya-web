from django.urls import path
from samarapp import views
from . import views

app_name = 'contact'

urlpatterns=[
    # path('contact/',views.contact,name='contact'),
    path('showform/',views.showform,name='showform'),
]
