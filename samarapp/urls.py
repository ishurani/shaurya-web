from django.urls import path
from samarapp import views
urlpatterns=[

path('about/',views.about,name='about'),
path('games/',views.games,name='games'),

]
