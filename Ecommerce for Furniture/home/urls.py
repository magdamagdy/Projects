from django.urls import path
from . import views
from django.urls import path
from django.conf.urls import url
from .views import Chairs, Armchairs, Sofas, Beds, Chaiselongues, Wardrobes, Shelving_units, Tables, remove_from_wish, \
    rating_review_chairs, rating_review_armchairs, rating_review_sofas, rating_review_beds, rating_review_chaiselongues, \
    rating_review_wardrobes, rating_review_shelving_units, rating_review_tables

urlpatterns = [

    path('', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('reg/', views.reg, name='reg'),
    path('seller/', views.seller, name='seller'),
    path('buyer/', views.buyer, name='buyer'),
    path('chairs/', views.chairs, name='chairs'),
    path('armchairs/', views.armchairs, name='armchairs'),
    path('sofas/', views.sofas, name='sofas'),
    path('beds/', views.beds, name='beds'),
    path('chaiselongues/', views.chaiselongues, name='chaiselongues'),
    path('shelving_units/', views.shelving_units, name='shelving_units'),
    path('tables/', views.tables, name='tables'),
    path('wardrobes/', views.wardrobes, name='wardrobes'),

    url(r'^Chairs/(?P<pk>\d+)$', Chairs, name='Chairs'),
    url(r'^Armchairs/(?P<pk>\d+)$', Armchairs, name='Armchairs'),
    url(r'^Beds/(?P<pk>\d+)$', Beds, name='Beds'),
    url(r'^Chaiselongues/(?P<pk>\d+)$', Chaiselongues, name='Chaiselongues'),
    url(r'^Sofas/(?P<pk>\d+)$', Sofas, name='Sofas'),
    url(r'^Wardrobes/(?P<pk>\d+)$', Wardrobes, name='Wardrobes'),
    url(r'^Shelving_units/(?P<pk>\d+)$', Shelving_units, name='Shelving_units'),
    url(r'^Tables/(?P<pk>\d+)$', Tables, name='Tables'),


    path('whishlist/', views.whishlist, name='whishlist'),
    url(r'^remove_from_wish/(?P<pk>\d+)$', remove_from_wish, name='remove_from_wish'),
    url(r'^rating_review_chairs/(?P<pk>\d+)$', rating_review_chairs, name='rating_review_chairs'),
    url(r'^rating_review_armchairs/(?P<pk>\d+)$', rating_review_armchairs, name='rating_review_armchairs'),
    url(r'^rating_review_sofas/(?P<pk>\d+)$', rating_review_sofas, name='rating_review_sofas'),
    url(r'^rating_review_beds/(?P<pk>\d+)$', rating_review_beds, name='rating_review_beds'),
    url(r'^rating_review_chaiselongues/(?P<pk>\d+)$', rating_review_chaiselongues, name='rating_review_chaiselongues'),
    url(r'^rating_review_wardrobes/(?P<pk>\d+)$', rating_review_wardrobes, name='rating_review_wardrobes'),
    url(r'^rating_review_shelving_units/(?P<pk>\d+)$', rating_review_shelving_units, name='rating_review_shelving_units'),
    url(r'^rating_review_tables/(?P<pk>\d+)$', rating_review_tables, name='rating_review_tables'),

]
