from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.showform, name='showform'),
    path('delete/<user_id>', views.delete, name='delete'),
    path('update/<user_id>', views.update, name='update'),
]
