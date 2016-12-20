from orchestrator.openstackOriApiUtil import *
# orchestrator

class orchestrator:
    # create new vnf through openstack(nova or tacker) by python ori api
    def new_vnf(self,vnf_info):
        nova_client = get_nova_clint()
        vnf=create_server(nova_client=nova_client, image_name=vnf_info.image_name, flavor_name=vnf_info.flavor_name,
                      network_name=vnf_info.network_name,
                      vm_name=vnf_info.vm_name, keypair_name=vnf_info.keypair_name, security_group_name=vnf_info.security_group_name,
                      compute_node_name=vnf_info.compute_node_name, user_data=vnf_info.user_data)
        return vnf
    def new_sfc(self):
        nova_client = get_nova_clint()
        create_server(nova_client=nova_client, image_name=image_name, flavor_name=flavor_name,
                      network_name=network_name,
                      vm_name=vm_name, keypair_name=keypair_name, security_group_name=security_group_name,
                      compute_node_name=compute_node_name, user_data=user_data)