from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('store.urls')),
    path('listings/', include('listings.urls')),

    # path('', include('pages.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
