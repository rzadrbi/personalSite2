from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from info import views as info_views


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('allauth.urls')),
                  path('', include('info.urls')),
                  path('blog/', include('blog.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = info_views.Handler404.as_view()


