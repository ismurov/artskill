from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'user_profile'

urlpatterns = [
    path('', login_required(views.ProfileView.as_view()), name='home'),
    path('favorites/', login_required(views.FavoritesView.as_view()), name='favorites'),
    path('orders/', login_required(views.OrdersView.as_view()), name='orders'),
]
