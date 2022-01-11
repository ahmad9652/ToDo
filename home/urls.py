from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name='Welcome'),
    path('contact',views.contact,name='Contact Us'),    
    path('about',views.about,name='About us'),   
    path('task',views.task1,name='Task List'),   
]