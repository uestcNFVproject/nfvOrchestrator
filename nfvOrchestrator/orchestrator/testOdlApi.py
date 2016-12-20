
from orchestrator.odlUtil import *

def testAll():
    print("sending service nodes")
    register_nodes(node_list=)

    print("sending service functions")
    register_vnfs(vnf_list=)

    print "sending service function forwarders"
    register_sffs(sff_list=)

    print "sending service function chains"
    register_sfcs(sfc_list=)

    print "sending service function metadata"
    register_sf_metadata_data()

    print "sending service function paths"
    register_sfps(sfp_list=)

    print "sending service function acl"
    register_acls(acl_list=)

    print "sending rendered service path"
    register_rsp(rsp=)

    print "sending rendered service path2"
    register_rsp(rsp=)


    print "sending service function classifiers"
    register_classifiers(classifier_list=)
