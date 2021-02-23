from django.urls import path, include
from . import views

app_name="chirp"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('upvote/<int:chirp_id>', views.upvote, name='upvote'),
]