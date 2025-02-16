from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.home, name='home'),
    path('route/<int:route_id>/', views.route_detail, name='route_detail'),
    path('route/<int:route_id>/create_event/', views.create_event, name='create_event'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]


