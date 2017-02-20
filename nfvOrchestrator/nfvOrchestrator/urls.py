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

from orchestrator.views import vnffgdListView
from orchestrator.views import vnffgdHandlerView
from orchestrator.views import vnffgdAddView
from orchestrator.views import vnffgdDeleteView

from orchestrator.views import nsdListView
from orchestrator.views import nsdHandlerView
from orchestrator.views import nsdAddView
from orchestrator.views import nsdDeleteView

from orchestrator.views import vnfListView
from orchestrator.views import vnfDeployView
from orchestrator.views import vnfDestoryView
from orchestrator.views import vnfHandlerView

from orchestrator.views import vnffgListView
from orchestrator.views import vnffgDeployView
from orchestrator.views import vnffgDestoryView
from orchestrator.views import vnffgHandlerView

from orchestrator.views import nsListView
from orchestrator.views import nsDeployView
from orchestrator.views import nsDestoryView
from orchestrator.views import nsHandlerView

from orchestrator.views import ns_algorithm_handler
from orchestrator.views import nsActiveAlgorithm
from orchestrator.views import nsAlgorithmListView
from orchestrator.views import activeNsAlgorithm
from orchestrator.views import addNsAlgorithm

from orchestrator.views import vnffg_algorithm_handler
from orchestrator.views import vnffgActiveAlgorithm
from orchestrator.views import vnffgAlgorithmListView
from orchestrator.views import activeVnffgAlgorithm
from orchestrator.views import addVnffgAlgorithm

from orchestrator.views import vnf_algorithm_handler
from orchestrator.views import vnfActiveAlgorithm
from orchestrator.views import vnfAlgorithmListView
from orchestrator.views import activeVnfAlgorithm
from orchestrator.views import addVnfAlgorithm

from orchestrator.views import computeNodeListView
from orchestrator.views import switchNodeListView
from orchestrator.views import TestView
from orchestrator.views import moniter
urlpatterns = [
    url(r'^test/$', TestView.as_view(), name='test'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', WelcomeView.as_view(), name='welcome'),
    url(r'^main/$', MainView.as_view(), name='main'),
    # rsp info for odl
    url(r'^rspget/$', rspSFNameListView.as_view(), name='rspSFNameListGet'),
    # demo
    url(r'^main/demodeploy/$', demodeployView.as_view(), name='demodeployPost'),
    # vnfd curd
    url(r'^main/vnfd_list/$', vnfdListView.as_view(), name='vnfdlistGet'),
    url(r'^main/vnfd_add$', vnfdAddView.as_view(), name='vnfdadd'),
    url(r'^main/vnfd_delete$', vnfdDeleteView.as_view(), name='vnfddelete'),
    url(r'^main/vnfd_handler/$', vnfdHandlerView.as_view(), name='vnfdhandler'),
    # vnffgd curd
    url(r'^main/vnffgd_list$', vnffgdListView.as_view(), name='vnffgdlistGet'),
    url(r'^main/vnffgd_add$', vnffgdAddView.as_view(), name='vnffgdadd'),
    url(r'^main/vnffgd_delete$', vnffgdDeleteView.as_view(), name='vnffgddelete'),
    url(r'^main/vnffgd_handler/$', vnffgdHandlerView.as_view(), name='vnffgdhandler'),

    # nsd curd
    url(r'^main/nsd_list$', nsdListView.as_view(), name='nsdlistGet'),
    url(r'^main/nsd_add$', nsdAddView.as_view(), name='nsddadd'),
    url(r'^main/nsd_delete$', nsdDeleteView.as_view(), name='nsddelete'),
    url(r'^main/nsd_handler/$', nsdHandlerView.as_view(), name='nsdhandler'),

    # vnf curd
    url(r'^main/vnf_list$', vnfListView.as_view(), name='vnflistGet'),
    url(r'^main/deploy_vnf$', vnfDeployView.as_view(), name='vnfDeploy'),
    url(r'^main/destory_vnf$', vnfDestoryView.as_view(), name='vnfDestory'),
    url(r'^main/vnf_handler/$', vnfHandlerView.as_view(), name='nsdhandler'),
    # vnffg curd
    url(r'^main/vnffg_list$', vnffgListView.as_view(), name='nsdlistGet'),
    url(r'^main/deploy_vnffg$', vnffgDeployView.as_view(), name='nsddadd'),
    url(r'^main/destory_vnffg$', vnffgDestoryView.as_view(), name='nsddelete'),
    url(r'^main/vnffg_handler/$', vnffgHandlerView.as_view(), name='nsdhandler'),
    # ns curd
    url(r'^main/ns_list$', nsListView.as_view(), name='nsdlistGet'),
    url(r'^main/deploy_ns$', nsDeployView.as_view(), name='nsddadd'),
    url(r'^main/destory_ns$', nsDestoryView.as_view(), name='nsddelete'),
    url(r'^main/ns_handler/$', nsHandlerView.as_view(), name='nsdhandler'),

    # ns algorithm
    url(r'^main/ns_algorithm_list$', nsAlgorithmListView.as_view(), name='ns algorithm list'),
    url(r'^main/ns_active_algorithm$', nsActiveAlgorithm.as_view(), name='ns_active_algorithm$'),
    url(r'^main/active_ns_algorithm$', activeNsAlgorithm.as_view(), name='active_ns_algorithm$'),
    url(r'^main/add_ns_algorithm$', addNsAlgorithm.as_view(), name='add_ns_algorithm$'),
    url(r'^main/ns_algorithm_handler/$', ns_algorithm_handler.as_view(), name='add_ns_algorithm$'),

    # vnffg algorithm
    url(r'^main/vnffg_algorithm_list$', vnffgAlgorithmListView.as_view(), name='vnffg_algorithm_list$'),
    url(r'^main/vnffg_active_algorithm$', vnffgActiveAlgorithm.as_view(), name='vnffg_active_algorithm$'),
    url(r'^main/active_vnffg_algorithm$', activeVnffgAlgorithm.as_view(), name='active_vnffg_algorithm$'),
    url(r'^main/add_vnffg_algorithm$', addVnffgAlgorithm.as_view(), name='add_vnffg_algorithm$'),
    url(r'^main/vnffg_algorithm_handler/$', vnffg_algorithm_handler.as_view(), name='add_vnffg_algorithm$'),

    # vnf algorithm
    url(r'^main/vnf_algorithm_list$', vnfAlgorithmListView.as_view(), name='vnffg_algorithm_list$'),
    url(r'^main/vnf_active_algorithm$', vnfActiveAlgorithm.as_view(), name='vnffg_active_algorithm$'),
    url(r'^main/active_vnf_algorithm$', activeVnfAlgorithm.as_view(), name='active_vnffg_algorithm$'),
    url(r'^main/add_vnf_algorithm$', addVnfAlgorithm.as_view(), name='add_vnffg_algorithm$'),
    url(r'^main/vnf_algorithm_handler/$', vnf_algorithm_handler.as_view(), name='add_vnffg_algorithm$'),

    # nfvi
    url(r'^main/compute_node_list$', computeNodeListView.as_view(), name='nsdlistGet'),
    url(r'^main/switch_node_list$', switchNodeListView.as_view(), name='nsdlistGet'),
    # vim
    url(r'^node_info/details/$', moniter.as_view(), name='nodeinfo'),
]
