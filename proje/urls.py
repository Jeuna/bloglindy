from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from django.contrib.auth import views as auth_views
from blog import views
from django.conf import settings
from django.conf.urls import include






urlpatterns = [
    url(r'^lindy/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^detail/(?P<url>[^/]*)/$', views.detail, name='detail'),
    url(r'^logout/$', auth_views.LogoutView.as_view(),{'next_page': 'logout.html'},name='logout'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)