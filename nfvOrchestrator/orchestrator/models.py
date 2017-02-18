# #-*-coding:utf-8 -*-
from django.db import models
import json
# Create your models here.

# class nsd(models.Model):
#     nsd_id = models.AutoField(primary_key=True)
#     # 定义原文
#     ori_descirption=models.CharField(max_length=20000,blank=False)
#     # 属性
#     description = models.CharField(max_length=200, blank=False)
#     metadata= models.CharField(max_length=200, blank=False)
#     imports=models.CharField(max_length=200, blank=False)
#     # 包含了vnf，cp，vl，fwp，groups的信息
#     # vnf中包含了type，properties中包含了flavor，auto-scale信息，requirements中包含了vl信息
#     # cp包含了cp所在vl的信息
#     # fwp中重要的是requiremets，包含了连接点的序列
#     # groups包含了group中的vnf，对应的fwp信息
#     topology_template = models.CharField(max_length=200, blank=True)
#
#
# class vnfd(models.Model):
#     vnfd_id=models.AutoField(primary_key=True)
#     nsd_id=models.ForeignKey(nsd.nsd_id)
#     # 定义原文
#     ori_descirption = models.CharField(max_length=20000, blank=False)
#     # 属性
#     vender=models.CharField(max_length=200, blank=False)
#     version=models.CharField(max_length=200, blank=False)
#     name=models.CharField(max_length=200, blank=False)
#     type=models.CharField(max_length=200, blank=False)
#     endpoint=models.CharField(max_length=200, blank=False)
#     configurations=models.CharField(max_length=200, blank=False)
#     lifecycle_events=models.CharField(max_length=200, blank=False)
#     deployment_flavour=models.CharField(max_length=200, blank=False)
#
# class vld(models.Model):
#     vld_id=models.AutoField(primary_key=True)
#     vnfd_id=models.ForeignKey(vnfd.vnfd_id)
#     nsd_id=models.ForeignKey(nsd.nsd_id)
#     # fgd_id=models.ForeignKey(fgd.fgd_id)
#     # 定义原文
#     ori_descirption = models.CharField(max_length=20000, blank=False)
#     # 属性
#     name=models.CharField(max_length=200,blank=True)
#
# class vdud(models.Model):
#     vdud_id=models.AutoField(primary_key=True)
#     vnfd_id=models.ForeignKey(vnfd.vnfd_id)
#     # 定义原文
#     ori_descirption = models.CharField(max_length=20000, blank=False)
#     # 属性
#     vm_image=models.CharField(max_length=200, blank=False)
#     vimInstanceName=models.CharField(max_length=200, blank=False)
#     scale_in_out=models.CharField(max_length=200, blank=False)
#
#
# class vnfcd(models.Model):
#     vnfcd_id=models.AutoField(primary_key=True)
#     vdud_id=models.ForeignKey(vdud.vdud_id)
#     # 定义原文
#     ori_descirption = models.CharField(max_length=20000, blank=False)
#     # 属性
#     connection_point=models.CharField(max_length=200, blank=False)
#
# class cpd(models.Model):
#     cpd_id=models.AutoField(primary_key=True)
#     nsd_id=models.ForeignKey(nsd.nsd_id)
#     vnfd_id=models.ForeignKey(vnfd.vnfd_id)
#     # 定义原文
#     ori_descirption = models.CharField(max_length=20000, blank=False)
#     # 属性
#     type=models.CharField(max_length=200, blank=False)
#     requirements=models.CharField(max_length=200, blank=False)
#
# class fgd(models.Model):
#     fgd_id=models.AutoField(primary_key=True)
#     nsd_id=models.ForeignKey(nsd.nsd_id)
#     # 定义原文
#     ori_descirption = models.CharField(max_length=20000, blank=False)
#     # 属性
#     type=models.CharField(max_length=200, blank=False)
#     description=models.CharField(max_length=200, blank=False)
#     vendor=models.CharField(max_length=200, blank=False)
#     version=models.CharField(max_length=200, blank=False)
#     vls=models.CharField(max_length=200, blank=False)
#     vnfs=models.CharField(max_length=200, blank=False)
#     forwarding_paths=models.CharField(max_length=200, blank=False)
#
#
# class fpd(models.Model):
#     fpd_id=models.AutoField(primary_key=True)
#     fgd_id=models.ForeignKey(fgd.fgd_id)
#     # 定义原文
#     ori_descirption = models.CharField(max_length=20000, blank=False)
#     # 属性
#     type=models.CharField(max_length=200, blank=False)
#     description=models.CharField(max_length=200, blank=False)
#     policy=models.CharField(max_length=200, blank=False)
#     requirements=models.CharField(max_length=200, blank=False)

class rsp(models.Model):
    rspRequestId=models.BigIntegerField()
    sfNameList=models.CharField(max_length=2000,blank=True)


class Descriptor(models.Model):
    # 0==》vnfd
    # 1==>vnffgd
    # 2==>nsd
    type=models.IntegerField()
    yaml_content=models.CharField(max_length=2000,blank=True)
    assigned_id=models.IntegerField()

class Node_info(models.Model):
    BaseInfo = models.CharField(max_length=2000, blank=True)
    NodeName = models.CharField(max_length=2000, blank=True)
    Time = models.CharField(max_length=2000, blank=True)
    RunTime = models.CharField(max_length=2000, blank=True)
    LoadInfo = models.CharField(max_length=2000, blank=True)
    Load1 = models.FloatField()
    Load5 = models.FloatField()
    Load15 = models.FloatField()
    TaskInfo = models.CharField(max_length=2000, blank=True)
    Taskstotal = models.IntegerField()
    TaskRunning = models.IntegerField()
    TaskSleeping = models.IntegerField()
    TaskStopped = models.IntegerField()
    Taskzombie = models.IntegerField()
    CpuInfo = models.CharField(max_length=2000, blank=True)
    Us = models.FloatField()
    Sy = models.FloatField()
    Ni = models.FloatField()
    Idle = models.FloatField()
    Wa = models.FloatField()
    Hi = models.FloatField()
    Si = models.FloatField()
    MemInfo = models.CharField(max_length=2000, blank=True)
    Memtotal = models.IntegerField()
    Memused = models.IntegerField()
    Memfree = models.IntegerField()
    Membuffer = models.IntegerField()
    DiskInfo = models.CharField(max_length=2000, blank=True)
    # FileSysName = models.CharField(max_length=2000, blank=True)
    # FileSysTotal = models.IntegerField()
    # FileSysFree = models.IntegerField()
    # MountPoint = models.CharField(max_length=2000, blank=True)
    IOinfo = models.CharField(max_length=2000, blank=True)
    # DeviceName = models.CharField(max_length=2000, blank=True)
    # Tps = models.FloatField()
    # ReadSpeed = models.FloatField()
    # ReadToral = models.IntegerField()
    # WriteSpeed = models.FloatField()
    # WriteTotal = models.IntegerField()
