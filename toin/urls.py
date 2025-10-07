from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from pages import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Language switcher route
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Your app routes
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
