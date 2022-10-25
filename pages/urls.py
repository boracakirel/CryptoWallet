from django.urls import path
from pages.views import AboutView, ContactView
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('currencies/', views.currency, name='currencies'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/', views.search, name='search'),
    path('coins/<str:coin_id>', views.coin_detail, name='detail'),
]
