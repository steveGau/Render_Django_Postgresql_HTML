from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace="blog"))
]

sqlite_database_ID=0
if sqlite_database_ID==1:
    urlpatterns += staticfiles_urlpatterns()

# path('home/', TemplateView.as_view(template_name="home.html")),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
