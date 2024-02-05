from django.contrib import admin
from django.urls import path, include
from eduxationmain import views

urlpatterns = [
    path("", views.index, name='Home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='Home'),
    path('videos/', views.videos, name='videos'),
    path('quizes.html', views.quizes, name='quizes'),
    path('papers/', views.papers, name='papers'),
    path('social.html', views.social, name='social'),
    path('contact.html', views.contact, name='contact'),
  

    #quiz
    path('clang/', views.clang, name='clang'),
    path('quiz/', views.quiz, name='quiz'),

    #plalists
    path('cplus/', views.cplus, name='cplus'),
    path('dbms/', views.dbms, name='dbms'),
    path('dsalgo/', views.dsalgo, name='dsalgo'),
    path('java/', views.java, name='java'),
    path('php/', views.php, name='php'),
]
