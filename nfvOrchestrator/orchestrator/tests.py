# 加载yaml
import yaml

# 读取文件
f = open('./templates_examples/vnffgd_example.yaml')

# 导入
x = yaml.load(f)


# print(x['topology_template']['node_templates'])

sfp_list=[]

for (k, v) in x['topology_template']['node_templates'].items():
   if k.startswith('Forwarding_path'):
      tmp = {}
      tmp[k] = v
      sfp_list.append(tmp)

for dic in sfp_list:
   for (k,v) in dic.items():
      print(v['properties']['path'])
      for vnf_info in v['properties']['path']:
         print(vnf_info['forwarder'])