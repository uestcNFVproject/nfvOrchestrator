# -*- coding: utf-8 -*-
import json
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
from orchestrator.models import rsp

class WelcomeView(TemplateView):
    template_name = "welcome.html"

class MainView(TemplateView):
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
