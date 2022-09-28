from django.urls import path
from pages.views import AboutView, ContactView
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('currencies/', views.index, name='currencies'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
