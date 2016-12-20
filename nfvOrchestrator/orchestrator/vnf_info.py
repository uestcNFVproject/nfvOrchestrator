


class vnf_info:
    def __init__(self, vm_name, image_name="TestVM", flavor_name="my3g", network_name="admin_internal_net",
                 keypair_name="mykey", security_group_name="my", compute_node_name='node-49.domain.tld', user_data='''
                #!/bin/sh
                passwd ubuntu<<EOF
                ubuntu
                ubuntu
                EOF
                sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
                service ssh restart
                '''):
        self.vm_name = vm_name
        self.image_name = image_name
        self.flavor_name = flavor_name
        self.network_name = network_name
        self.keypair_name = keypair_name
        self.security_group_name = security_group_name
        self.compute_node_name = compute_node_name
        self.user_data=user_data
