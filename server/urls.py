from django.urls import path
from server import views

urlpatterns = [
    path('',views.index_page), 
    path('send',views.join_us), 
    path('quidroo',views.quidroo), 
]