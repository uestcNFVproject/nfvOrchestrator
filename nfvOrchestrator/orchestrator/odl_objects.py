


class vnfInfo:
    def __init__(self, vm_name,vnf_name,ip_mgmt_address,rest_uri,sf_data_plane_locator_ip, type,service_function_forwarder_name,sf_data_plane_locator_name="eth1",image_name="TestVM", flavor_name="my3g", network_name="admin_internal_net",
                 keypair_name="mykey", security_group_name="my", compute_node_name='node-49.domain.tld', sf_dpl_name="eth1",
                 user_data='''
                #!/bin/sh
                passwd ubuntu<<EOF
                ubuntu
                ubuntu
                EOF
                sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
                service ssh restart
                '''):
        self.vm_name = vm_name
        self.vnf_name=vnf_name
        self.ip_mgmt_address=ip_mgmt_address
        self.rest_uri=rest_uri
        self.sf_data_plane_locator_ip=sf_data_plane_locator_ip
        self.sf_data_plane_locator_name=sf_data_plane_locator_name
        self.service_function_forwarder_name=service_function_forwarder_name
        self.type=type
        self.image_name = image_name
        self.flavor_name = flavor_name
        self.network_name = network_name
        self.keypair_name = keypair_name
        self.security_group_name = security_group_name
        self.compute_node_name = compute_node_name
        self.sf_dpl_name=sf_dpl_name
        self.user_data=user_data
