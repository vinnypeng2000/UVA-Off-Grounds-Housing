from django.urls import path, include
from .import views
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'app'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Filter paths
    path('filter/', views.FilterView, name='filter'),
    path('filter/<str:name>', views.PropertyView, name='property'),

    # Map paths
    path('map/', views.MapView.as_view(), name='map'),

    # About
    path('about/', views.AboutView.as_view(), name='about'),

    # Search
    path('search_housing/', views.search_housing, name='search_housing')
]
