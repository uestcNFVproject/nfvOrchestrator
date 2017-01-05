# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
from orchestrator.models import rsp
from orchestrator.demodeploy import Demo_deploy
from orchestrator import NFVO

class WelcomeView(TemplateView):
    template_name = "welcome.html"

class MainView(TemplateView):
    NFVO.init_NFVO(vim=None, vnfm=None, NSD_manager=None, VNFD_manager=None, NS_manager=None, NFVI_manager=None,algorith_manager=None,FG_manager=None)
    template_name = "main.html"


#

# odl request for rsp's sf name list
class rspSFNameListView(View):
    def get(self, request, *args, **kwargs):
        if(request.method=="GET"):
            resRequestID=request.GET.get('rspID',-1)
            if resRequestID!=-1:
                # 根据resRequestID在数据库中查询
                try:
                    p=rsp.objects.get(rspRequestId=resRequestID)
                except rsp.DoesNotExist:
                    return HttpResponse(json.dumps("no rsp found in db"), content_type="application/json")
                p.sfNameList=json.loads(p.sfNameList)
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
    def post(self,request, *args, **kwargs):
        if (request.method == "POST"):
            demotype = request.POST.get('demotype', -1)
            demo_deploy=Demo_deploy()
            demo_deploy.deploy_demo(demotype)
        else:
            return HttpResponse(json.dumps("please use post"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")



# handle vnfd list
class vnfdListView(View):
    def get(self,request, *args, **kwargs):
        vnfd_list=[]
        return HttpResponse(json.dumps(vnfd_list), content_type="application/json")

class vnfdAddView(TemplateView):
    template_name = "vnfd_add.html."

class vnfdDeleteView(TemplateView):
    template_name = "vnfd_delete.html."


# handle vnfd curd
class vnfdHandlerView(View):
    def post(self,request, *args, **kwargs):
        print("post")
        print(request)
        print(request.path)
        if (request.method == "POST"):
            demotype = request.POST.get('demotype', -1)
            demo_deploy=Demo_deploy()
            demo_deploy.deploy_demo(demotype)
        else:
            return HttpResponse(json.dumps("please use post"), content_type="application/json")
        return HttpResponse(json.dumps("wrong page"), content_type="application/json")