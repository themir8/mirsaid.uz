from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from main.views import Registration, LoginView, logout_view

urlpatterns = [
    path('course/', include('course.urls')),
    path('admin/', admin.site.urls, name='admin_panel'),
    path('mini-admin/', include('miniadmin.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path("ApiView/<int:pk>/", ApiView),
    path("signup/", Registration),
    path("login/", LoginView),
    path("logout/", logout_view),
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    path('blog/', include('blog.urls')),
    path('', include('main.urls')),
)