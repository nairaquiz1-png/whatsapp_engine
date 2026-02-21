from django.urls import path
from .views import landing_page  # only import landing_page

urlpatterns = [
    path('', landing_page),  # root URL
]