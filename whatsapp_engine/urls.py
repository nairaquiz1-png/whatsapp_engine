from django.contrib import admin
from django.urls import path, include  # ✅ make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marketing.urls')),  # ✅ this works now
]