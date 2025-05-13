from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
    path('', include('pwa.urls')),  # 👈 Include this li
    # path('manifest.json', TemplateView.as_view(template_name="manifest.json", content_type='application/json')),
    # path('sw.js', TemplateView.as_view(template_name="sw.js", content_type='application/javascript')),
]
