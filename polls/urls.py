from django.urls import path, re_path
from . import views
from .views import polls_details, polls_list

urlpatterns = [
    path(r'^$', views.index,name='index'),
    path('polls/', polls_list,name='polls_list'),
    path('polls/<int:pk>/', polls_details, name='polls_details')


]
