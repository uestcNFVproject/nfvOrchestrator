# -*- coding: utf-8 -*-
import json
import yaml

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View

from orchestrator.models import rsp
from orchestrator.demodeploy import Demo_deploy
from orchestrator import NFVO
from orchestrator import VIMProxy
from orchestrator import VNFM
from orchestrator import NSDcatalogue
from orchestrator import VNFDcatalogue
from orchestrator import NScatalogue
from orchestrator import NFVIcatalogue
from orchestrator import AlgorithmManager
from orchestrator import FG_manager

vim = VIMProxy.VIMProxy()
nfvo = NFVO.init_NFVO(vim=vim, vnfm=VNFM.VNFM_simple(), NSD_manager=NSDcatalogue.NSD_manager(),
                      VNFD_manager=VNFDcatalogue.VNFD_manager(), NS_manager=NScatalogue.NS_manager(),
                      NFVI_manager=NFVIcatalogue.NFVI_manager(), algorith_manager=AlgorithmManager.AlgorithmManager(),
                      FG_manager=FG_manager.FG_manager(vim))


class WelcomeView(TemplateView):
    template_name = "welcome.html"


class MainView(TemplateView):
    template_name = "main.html"


#

# odl request for rsp's sf name list
class rspSFNameListView(View):
    def get(self, request, *args, **kwargs):
        if (request.method == "GET"):
            resRequestID = request.GET.get('rspID', -1)
            if resRequestID != -1:
                # 根据resRequestID在数据库中查询
                try:
                    p = rsp.objects.get(rspRequestId=resRequestID)
                except rsp.DoesNotExist:
                    return HttpResponse(json.dumps("no rsp found in db"), content_type="application/json")
                p.sfNameList = json.loads(p.sfNameList)
                json_str = json.dumps(p, default=lambda o: o.__dict__, sort_keys=True, indent=4)
                return HttpResponse(json_str, content_type="application/json")
            else:
                return HttpResponse(json.dumps("no resRequestID found"), content_type="application/json")
        else:
            return HttpResponse(json.dumps("no post support"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")


#
# handle demo deploy request
class demodeployView(View):
    def post(self, request, *args, **kwargs):
        if (request.method == "POST"):
            demotype = request.POST.get('demotype', -1)
            demo_deploy = Demo_deploy()
            demo_deploy.deploy_demo(demotype)
        else:
            return HttpResponse(json.dumps("please use post"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")


# handle vnfd list
class vnfdListView(View):
    def get(self, request, *args, **kwargs):
        global nfvo
        vnfd_list = nfvo.find_all_vnfd()

        vnfd_content_list = []
        for vnfd in vnfd_list:
            vnfd_content_list.append(yaml.dump(vnfd.yaml_content))
        return HttpResponse(json.dumps(vnfd_content_list), content_type="application/json")


class vnfdAddView(TemplateView):
    template_name = "vnfd_add.html."


class vnfdDeleteView(TemplateView):
    template_name = "vnfd_delete.html."


# handle vnfd curd
class vnfdHandlerView(View):
    def post(self, request, *args, **kwargs):
        global nfvo
        if request.path == '/main/vnfd_add/vnfd_handler/':
            if (request.method == "POST"):
                vnfd = request.POST.get('vnfd', None)
                if vnfd is None:
                    return HttpResponse(json.dumps("no vnfd"), content_type="application/json")
                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.upload_vnfd(vnfd)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        if request.path == '/main/vnfd_delete/vnfd_handler/':
            if (request.method == "POST"):
                vnfd_name = request.POST.get('vnfdname', None)
                if vnfd_name is None:
                    return HttpResponse(json.dumps("no vnfd_name"), content_type="application/json")

                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.delete_vnfd_by_name(vnfd_name)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")


# handle vnffgd list
class vnffgdListView(View):
    def get(self, request, *args, **kwargs):
        global nfvo
        vnffgd_list = nfvo.find_all_vnffgd()

        vnffgd_content_list = []
        for vnffgd in vnffgd_list:
            vnffgd_content_list.append(yaml.dump(vnffgd.yaml_content))
        return HttpResponse(json.dumps(vnffgd_content_list), content_type="application/json")


class vnffgdAddView(TemplateView):
    template_name = "vnffgd_add.html."


class vnffgdDeleteView(TemplateView):
    template_name = "vnffgd_delete.html."


# handle vnffgd curd
class vnffgdHandlerView(View):
    def post(self, request, *args, **kwargs):
        global nfvo
        if request.path == '/main/vnffgd_add/vnffgd_handler/':
            if (request.method == "POST"):
                vnffgd = request.POST.get('vnffgd', None)
                if vnffgd is None:
                    return HttpResponse(json.dumps("no vnffgd"), content_type="application/json")
                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.upload_vnffgd(vnffgd)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        if request.path == '/main/vnffgd_delete/vnffgd_handler/':
            if (request.method == "POST"):
                vnffgd_name = request.POST.get('vnffgdname', None)
                if vnffgd_name is None:
                    return HttpResponse(json.dumps("no vnffgd_name"), content_type="application/json")

                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.delete_vnffgd_by_name(vnffgd_name)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")


# handle nsd list
class nsdListView(View):
    def get(self, request, *args, **kwargs):
        global nfvo
        nsd_list = nfvo.find_all_nsd()
        nsd_content_list = []
        for nsd in nsd_list:
            nsd_content_list.append(yaml.dump(nsd.yaml_content))
        return HttpResponse(json.dumps(nsd_content_list), content_type="application/json")


class nsdAddView(TemplateView):
    template_name = "nsd_add.html."


class nsdDeleteView(TemplateView):
    template_name = "nsdd_delete.html."


# handle nsd curd
class nsdHandlerView(View):
    def post(self, request, *args, **kwargs):
        global nfvo
        if request.path == '/main/nsd_add/nsd_handler/':
            if (request.method == "POST"):
                nsd = request.POST.get('nsd', None)
                if nsd is None:
                    return HttpResponse(json.dumps("no nsd"), content_type="application/json")
                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.upload_nsd(nsd)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        if request.path == '/main/nsd_delete/nsd_handler/':
            if (request.method == "POST"):
                nsd_name = request.POST.get('nsdname', None)
                if nsd_name is None:
                    return HttpResponse(json.dumps("no nsd_name"), content_type="application/json")

                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.delete_nsd_by_name(nsd_name)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")

# handle vnf list
class vnfListView(View):
    def get(self, request, *args, **kwargs):
        global nfvo
        vnf_list = nfvo.get_all_vnf_instances();
        return HttpResponse(json.dumps(vnf_list), content_type="application/json")

class vnfDeployView(TemplateView):
    template_name = "vnf_deploy.html."


class vnfDestoryView(TemplateView):
    template_name = "vnf_destory.html."


# handle vnf curd
class vnfHandlerView(View):
    def post(self, request, *args, **kwargs):
        global nfvo
        if request.path == '/main/deploy_vnf/vnf_handler/':
            if (request.method == "POST"):
                vnfd_name = request.POST.get('vnfd_name', None)
                vnf_instance_name = request.POST.get('vnf_instance_name', None)
                if vnfd_name is None:
                    return HttpResponse(json.dumps("no vnfd_name"), content_type="application/json")
                if vnf_instance_name is None:
                    return HttpResponse(json.dumps("no vnf_instance_name"), content_type="application/json")
                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.deploy_vnf_instance_by_vnfd_name(vnfd_name,vnf_instance_name)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        if request.path == '/main/destory_vnf/vnf_handler/':
            if (request.method == "POST"):
                vnf_instance_name = request.POST.get('vnf_instance_name', None)
                if vnf_instance_name is None:
                    return HttpResponse(json.dumps("no vnf_instance_name"), content_type="application/json")

                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.destory_vnf_instance_by_name(vnf_instance_name)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")

class vnffgListView(View):
    def get(self, request, *args, **kwargs):
        global nfvo
        vnffg_list = nfvo.get_all_vnffg_instance()
        return HttpResponse(json.dumps(vnffg_list), content_type="application/json")

class vnffgDeployView(TemplateView):
    template_name = "vnffg_deploy.html."


class vnffgDestoryView(TemplateView):
    template_name = "vnffg_destory.html."


# handle nsd curd
class vnffgHandlerView(View):
    def post(self, request, *args, **kwargs):
        global nfvo
        if request.path == '/main/deploy_vnffg/vnffg_handler/':
            if (request.method == "POST"):
                vnffgd_name = request.POST.get('vnffgd_name', None)
                vnffg_instance_name = request.POST.get('vnffg_instance_name', None)
                if vnffgd_name is None:
                    return HttpResponse(json.dumps("no vnffgd_name"), content_type="application/json")
                if vnffg_instance_name is None:
                    return HttpResponse(json.dumps("no vnffg_instance_name"), content_type="application/json")
                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.deploy_vnffg_instance_by_vnffgd_name(vnffgd_name,vnffg_instance_name)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        if request.path == '/main/destory_vnffg/vnffg_handler/':
            if (request.method == "POST"):
                vnffg_instance_name = request.POST.get('vnffg_instance_name', None)
                if vnffg_instance_name is None:
                    return HttpResponse(json.dumps("no vnffg_instance_name"), content_type="application/json")

                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.destory_vnffg_instance_by_name(vnffg_instance_name)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")


class nsListView(View):
    def get(self, request, *args, **kwargs):
        global nfvo
        ns_list = nfvo.get_all_ns_instance()
        return HttpResponse(json.dumps(ns_list), content_type="application/json")

class nsDeployView(TemplateView):
    template_name = "ns_deploy.html."


class nsDestoryView(TemplateView):
    template_name = "ns_destory.html."


# handle ns curd
class nsHandlerView(View):
    def post(self, request, *args, **kwargs):
        global nfvo
        if request.path == '/main/deploy_ns/ns_handler/':
            if (request.method == "POST"):
                nsd_name = request.POST.get('nsd_name', None)
                ns_instance_name = request.POST.get('ns_instance_name', None)
                if nsd_name is None:
                    return HttpResponse(json.dumps("no nsd_name"), content_type="application/json")
                if ns_instance_name is None:
                    return HttpResponse(json.dumps("no ns_instance_name"), content_type="application/json")
                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.deploy_ns_instance_by_nsd_name(nsd_name,ns_instance_name)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        if request.path == '/main/destory_ns/ns_handler/':
            if (request.method == "POST"):
                ns_instance_name = request.POST.get('ns_instance_name', None)
                if ns_instance_name is None:
                    return HttpResponse(json.dumps("no ns_instance_name"), content_type="application/json")

                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.destory_ns_instance_by_name(ns_instance_name)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")

# algorithm
class algorithmListView(View):
    def get(self, request, *args, **kwargs):
        global nfvo
        algorithm_list = nfvo.get_all_alogorithm()
        return HttpResponse(json.dumps(algorithm_list), content_type="application/json")


class algorithmAddView(TemplateView):
    template_name = "algorithm_add.html."



class algorithmDeleteView(TemplateView):
    template_name = "algorithm_delete.html."


# handle algorithm curd
class algorithmHandlerView(View):
    def post(self, request, *args, **kwargs):
        global nfvo
        if request.path == '/main/algorithm_add/algorithm_handler/':
            if (request.method == "POST"):
                algorithm_name = request.POST.get('algorithm_name', None)
                algorithm_content = request.POST.get('algorithm_content', None)
                if algorithm_name is None:
                    return HttpResponse(json.dumps("no algorithm_name"), content_type="application/json")
                if algorithm_content is None:
                    return HttpResponse(json.dumps("no algorithm_content"), content_type="application/json")
                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.upload_alorithm(algorithm_name,algorithm_content)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        if request.path == '/main/algorithm_delete/algorithm_handler/':
            if (request.method == "POST"):
                algorithm_name = request.POST.get('algorithm_name', None)
                if algorithm_name is None:
                    return HttpResponse(json.dumps("no algorithm_name"), content_type="application/json")

                if nfvo is None:
                    return HttpResponse(json.dumps("nfvo not init"), content_type="application/json")
                try:
                    nfvo.delete_alorithm(algorithm_name)
                except Exception as e:
                    return HttpResponse(json.dumps(str(e)), content_type="application/json")
                return HttpResponse(json.dumps("ok"), content_type="application/json")
            else:
                return HttpResponse(json.dumps("please use post"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")


# compute_node
class computeNodeListView(View):
    def get(self, request, *args, **kwargs):
        global nfvo
        compute_node_list = nfvo.get_all_compute_node()
        return HttpResponse(json.dumps(compute_node_list), content_type="application/json")

# switch_node
class switchNodeListView(View):
    def get(self, request, *args, **kwargs):
        global nfvo
        switch_node_list = nfvo.get_all_switch_node()
        return HttpResponse(json.dumps(switch_node_list), content_type="application/json")
