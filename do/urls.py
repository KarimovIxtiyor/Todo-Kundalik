from django.urls import path
from .views import IndexView,TodoActionView,about_views

urlpatterns=[
    path('',IndexView.as_view(),name='index'),
    path('<int:todo_id>/<str:action>/action/', TodoActionView.as_view(),name='action'),
    path('about/',about_views,name='about'),
]