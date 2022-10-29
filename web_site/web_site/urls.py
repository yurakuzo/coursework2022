from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()
admin.site.enable_nav_sidebar = False
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('services/', include('service.urls'))
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
