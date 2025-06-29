from django.urls import path
from . import views 
urlpatterns=[
    path('',views.index,name='index'),
    path('explore/<int:id>/', views.explore, name='explore_page'),
]