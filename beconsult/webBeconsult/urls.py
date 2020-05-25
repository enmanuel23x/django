from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from webBeconsult import views


urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^admin/', admin.site.urls),
    
    
]
if True:
    urlpatterns += static(settings.MEDIA_URL, documentS_root=settings.MEDIA_ROOT)