from django.urls import path
from .views import homepage, fetch_data
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('',homepage, name='home'),
    path('', fetch_data, name='display_data'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
