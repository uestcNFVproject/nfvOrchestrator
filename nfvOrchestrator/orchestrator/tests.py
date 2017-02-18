# 加载yaml
import yaml
import re
# # 读取文件
# f = open('./templates_examples/vnffgd_example.yaml')
#
# # 导入
# x = yaml.load(f)
#
#
# # print(x['topology_template']['node_templates'])
#
# sfp_list=[]
#
# for (k, v) in x['topology_template']['node_templates'].items():
#    if k.startswith('Forwarding_path'):
#       tmp = {}
#       tmp[k] = v
#       sfp_list.append(tmp)
#
# for dic in sfp_list:
#    for (k,v) in dic.items():
#       print(v['properties']['path'])
#       for vnf_info in v['properties']['path']:
#          print(vnf_info['forwarder'])


def testTop():
   msg='''top - 10:07:53 up 7 min,  1 user,  load average: 0.86, 1.31, 0.77
Tasks: 172 total,   1 running, 171 sleeping,   0 stopped,   0 zombie
%Cpu(s): 43.0 us,  6.4 sy,  0.5 ni, 48.9 id,  0.5 wa,  0.0 hi,  0.7 si,  0.0 st
KiB Mem:   2049120 total,  1973456 used,    75664 free,    73864 buffers
KiB Swap:  1046524 total,      228 used,  1046296 free.   616664 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 2271 py        20   0 3660064 592056  43496 S  75.4 28.9   3:56.71 java
 1961 py        20   0 1261324 201448  63856 S  37.7  9.8   1:53.20 compiz
 1073 root      20   0  445664 148628  28064 S   6.3  7.3   0:44.13 Xorg
 2694 py        20   0   29012   3116   2708 R   6.3  0.2   0:00.01 top

top - 10:07:56 up 7 min,  1 user,  load average: 0.80, 1.29, 0.77
Tasks: 172 total,   1 running, 171 sleeping,   0 stopped,   0 zombie
%Cpu(s): 10.9 us,  2.4 sy,  0.0 ni, 86.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:   2049120 total,  1973484 used,    75636 free,    73864 buffers
KiB Swap:  1046524 total,      228 used,  1046296 free.   616664 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 1961 py        20   0 1261324 201448  63856 S  14.6  9.8   1:53.64 compiz
 2271 py        20   0 3660064 592056  43496 S  10.3 28.9   3:57.02 java
 1073 root      20   0  445664 148628  28064 S   5.7  7.3   0:44.30 Xorg
 2467 py        20   0 2919004  58772  17232 S   0.3  2.9   0:04.54 java

'''
   res=re.split('top - ',msg)
   print('0:')
   print(res[0])
   print('1:')
   print(res[1])
   print('2:')
   print(res[2])
   print(res[3])

if __name__ == '__main__':
    testTop()