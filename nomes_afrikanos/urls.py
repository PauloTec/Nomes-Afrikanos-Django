"""nomes_afrikanos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views 

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

#IMPORTAR VIEWS ESPECÍFICOS
from nomes import views as nomes_views

urlpatterns = [
    path('admin/', admin.site.urls),

    #páginas iniciais
    #url(r'^$', views.index, name="index"),
    url(r'^$', nomes_views.lista_nomes, name="index"),
    url(r'^sobre/$', views.sobre, name="sobre"),
    url(r'^contacto/$', views.contacto),

    #Páginas dos aplicativos
    url(r'^nomes/', include('nomes.urls')),
    url(r'^contas/', include('contas.urls')), 
]

urlpatterns+=staticfiles_urlpatterns() #para ficheiros estáticos
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #para imagens
