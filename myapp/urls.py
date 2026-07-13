from django.urls import path
from . import views

urlpatterns = [
    # path('about/', views.about,  name='about'),

    path('aboutme', views.aboutme, name='aboutme'),
    path('now/', views.now, name='now'),
    path('hello/', views.hello, name='hello'),
    path('add/', views.add, name='add'),
    path('joke/', views.joke, name='joke'),
    path('password/', views.password, name='password'),
    path('count/', views.count, name='count'),
    path('hello-time/', views.hello_time, name='hello_time'),
    path('codecoin/', views.codecoin, name='codecoin'),
    path('languages/', views.languages, name='languages'),
    path('next-lesson/', views.next_lesson, name='next_lesson'),
]