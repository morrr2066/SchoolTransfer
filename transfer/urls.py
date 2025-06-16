from django.urls import path
from .views import apply_view,confirmation_view

urlpatterns = [
    path('', apply_view, name='apply'),
    path('confirmation/', confirmation_view, name='confirmation'),
]
