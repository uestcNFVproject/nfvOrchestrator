"""nfvOrchestrator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from orchestrator.views import WelcomeView
from orchestrator.views import MainView
from orchestrator.views import rspSFNameListView
from orchestrator.views import demodeployView
from orchestrator.views import vnfdListView
from orchestrator.views import vnfdHandlerView
from orchestrator.views import vnfdAddView
from orchestrator.views import vnfdDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', WelcomeView.as_view(), name='welcome'),
    url(r'^main/$', MainView.as_view(), name='main'),
    url(r'^rspget/$', rspSFNameListView.as_view(), name='rspSFNameListGet'),
    url(r'^main/demodeploy/$', demodeployView.as_view(), name='demodeployPost'),
    url(r'^main/vnfd_list/$', vnfdListView.as_view(), name='vnfdlistGet'),
    url(r'^main/vnfd_add/$', vnfdAddView.as_view(), name='vnfdadd'),
    url(r'^main/vnfd_delete/$', vnfdDeleteView.as_view(), name='vnfddelete'),
    url(r'^main/vnfd_handler/$', vnfdHandlerView.as_view(), name='vnfdhandler'),

]
