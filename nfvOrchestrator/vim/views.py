from django.shortcuts import render

import json
import yaml

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
from vim.models import Node_info
# Create your views here.
class moniter(View):
    def post(self, request, *args, **kwargs):
        # 处理localAgent上传的信息
        infoJson = request.GET.get('nodeinfo', None)
        if infoJson != None:
            # 进行存储
            # 根据resRequestID在数据库中查询
            try:
                node_info=Node_info( ** json.loads(infoJson))
                node_info.save()
            except Exception:
                return HttpResponse(json.dumps("message illegal"), content_type="application/json")
            return HttpResponse("ok", content_type="application/json")
        else:
            return HttpResponse(json.dumps("no nodeinfo found"), content_type="application/json")

    def get(self, request, *args, **kwargs):
        # 处理用户的请求
        nodeName = request.GET.get('nodeName', None)
        if nodeName != None:
            # 根据nodeName在数据库中查询
            try:
                p = Node_info.objects.get(NodeName=nodeName)
            except Node_info.DoesNotExist:
                return HttpResponse(json.dumps("no info found in db"), content_type="application/json")
            json_str = json.dumps(p, default=lambda o: o.__dict__, sort_keys=True, indent=4)
            return HttpResponse(json_str, content_type="application/json")
        else:
            # 提取所有信息
            try:
                p = Node_info.objects.all()
            except Node_info.DoesNotExist:
                return HttpResponse(json.dumps("no info found in db"), content_type="application/json")
            json_str = json.dumps(p, default=lambda o: o.__dict__, sort_keys=True, indent=4)
            return HttpResponse(json_str, content_type="application/json")

