from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("Welcome to the E-commerce API!")

urlpatterns = [
    path('', home),  # 👈 "/" shows welcome message
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
]

# 👇 This must come after urlpatterns is defined
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


