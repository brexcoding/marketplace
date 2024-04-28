from market.views import landingpage ,products , ordering 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include ,re_path
from django.contrib import admin



urlpatterns = [
    re_path("admin",admin.site.urls),# make sure to change the url for more security "security layer"
    path('' , landingpage ,name='home' ),
    re_path("products" ,  products , name="products"),
    path('order/<int:pk>/', ordering.as_view(), name='ordering') , # No change here
   

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)