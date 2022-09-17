from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('about/', views.about, name='about'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('price/', views.price, name='price'),
    path('docs/', views.docs, name='docs'),
    path('', views.post_list, name='home'),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



