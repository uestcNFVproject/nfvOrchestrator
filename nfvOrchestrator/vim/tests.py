from django.test import TestCase

# Create your tests here.

from django.db import models
from vim.models import Node_info
from django.test import TestCase

class Test(TestCase):
    def test(self):
        node_info = Node_info()
        node_info.BaseInfo = "BaseInfo"
        node_info.NodeName = "NodeName"





# node_info.Time = models.DateTimeField()
# print(node_info.Time)
# node_info.RunTime = models.CharField(max_length=2000, blank=True)
# node_info.LoadInfo = models.CharField(max_length=2000, blank=True)
# node_info.Load1 = models.FloatField(max_digits=10, decimal_places=2)
# node_info.Load5 = models.FloatField(max_digits=10, decimal_places=2)
# node_info.Load15 = models.FloatField(max_digits=10, decimal_places=2)
# node_info.TaskInfo = models.CharField(max_length=2000, blank=True)
# node_info.Taskstotal = models.IntegerField()
# node_info.TaskRunning = models.IntegerField()
# node_info.TaskSleeping = models.IntegerField()
# node_info.TaskStopped = models.IntegerField()
# node_info.Taskzombie = models.IntegerField()
# node_info.CpuInfo = models.CharField(max_length=2000, blank=True)
# node_info.Us = models.FloatField(max_digits=10, decimal_places=2)
# node_info.Sy = models.FloatField(max_digits=10, decimal_places=2)
# node_info.Ni = models.FloatField(max_digits=10, decimal_places=2)
# node_info.Id = models.FloatField(max_digits=10, decimal_places=2)
# node_info.Wa = models.FloatField(max_digits=10, decimal_places=2)
# node_info.Hi = models.FloatField(max_digits=10, decimal_places=2)
# node_info.Si = models.FloatField(max_digits=10, decimal_places=2)
# node_info.MemInfo = models.CharField(max_length=2000, blank=True)
# node_info.Memtotal = models.IntegerField()
# node_info.Memused = models.IntegerField()
# node_info.Memfree = models.IntegerField()
# node_info.Membuffer = models.IntegerField()
# node_info.DiskInfo = models.CharField(max_length=2000, blank=True)
# node_info.FileSysName = models.CharField(max_length=2000, blank=True)
# node_info.FileSysTotal = models.IntegerField()
# node_info.FileSysFree = models.IntegerField()
# node_info.MountPoint = models.CharField(max_length=2000, blank=True)
# node_info.IOinfo = models.CharField(max_length=2000, blank=True)
# node_info.DeviceName = models.CharField(max_length=2000, blank=True)
# node_info.Tps = models.FloatField(max_digits=10, decimal_places=2)
# node_info.ReadSpeed = models.FloatField(max_digits=10, decimal_places=2)
# node_info.ReadToral = models.IntegerField()
# node_info.WriteSpeed = models.FloatField(max_digits=10, decimal_places=2)
# node_info.WriteTotal = models.IntegerField()
