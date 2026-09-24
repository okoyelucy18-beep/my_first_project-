from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('monasteries/<slug:slug>/', views.monastery_detail, name='monastery_detail'),
    path('monasteries/holy-cross-nteje/', views.holy_cross, name='holy-cross'),
    path('monasteries/st-benedict-ozubulu/', views.st_benedict, name='st-benedict'),
    path('monasteries/carmelite-holy-family/', views.carmelite, name='carmelite'),
    path('retreats/', views.retreats, name='retreats'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('prayer-intentions/', views.prayer_intentions, name='prayer-intentions'),
    path('submit-prayer-intention/', views.submit_prayer_intention, name='submit_prayer_intention'),
    path('submit-retreat-request/', views.submit_retreat_request, name='submit_retreat_request'),
]