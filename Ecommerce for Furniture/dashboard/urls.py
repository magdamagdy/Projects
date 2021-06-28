from django.urls import path
from . import views
from django.conf.urls import url
from .views import remove_item

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),
    url(r'^remove_item/(?P<pk>\d+)$', remove_item, name='remove_item'),
]