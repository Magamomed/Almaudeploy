# myproject/urls.py

from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.application_form, name='application_form'),
    path('success/', views.success, name='success'),
    path('schedule_interview/', views.schedule_interview, name='schedule_interview'),
    path('schedule_event/', views.schedule_event, name='schedule_event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('', views.application_form),  # или views.home, если вы сделали отдельную домашнюю страницу
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
