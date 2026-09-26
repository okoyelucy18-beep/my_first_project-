
from django.contrib import admin  # type: ignore[reportMissingModuleSource]
from django.urls import include , path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Discover.urls'))
]
