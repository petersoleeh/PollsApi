from django.urls import path, re_path
from . import views
from .apiviews import PollList, PollDetail

urlpatterns = [
    # path(r'^$', views.index,name='index'),
    path('polls/', PollList.as_view(),name='polls_list'),
    path('polls/<int:pk>/', PollDetail.as_view, name='polls_detail')


]
