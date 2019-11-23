from django.urls import path
from samarapp import views
urlpatterns=[

path('about/',views.about,name='about'),
path('games/',views.games,name='games'),
path('gallery/',views.gallery,name='gallery'),
path('sponsers/',views.sponsers,name='sponsers'),
path('team/',views.team,name='team'),
]
