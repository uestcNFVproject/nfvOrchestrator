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

vim=VIMProxy.VIMProxy()
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
        vnfd_list =nfvo.find_all_vnfd()

        vnfd_content_list=[]
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
