from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.timeline,name='Timeline'),
    url(r'^comment/(?P<pk>\d+)',views.Comment_Image,name='image-comment'),
    url(r'^search/',views.search_results, name='search-results'),
    url(r'^profile/',views.profile, name='profile'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

