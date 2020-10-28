
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Tutorial'
admin.site.site_title = 'Welcome to the Tutorials'
admin.site.index_title = 'Welcome to this Portal'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('tinymce/', include('tinymce.urls')),
    
]
