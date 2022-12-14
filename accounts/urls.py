from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.add_crypto, name='add_crypto'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transactions/<str:coin_id>', views.transactions, name='transactions'),
    path('edit_transaction/', views.edit_transaction, name='edit'),
    path('transactions/<str:coin_id>/delete/<int:transaction_id>', views.delete_transaction, name='delete'),
]
