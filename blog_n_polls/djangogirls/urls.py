from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('polls/', include('polls.urls')),
    url(r'', include('blog.urls')),
]
