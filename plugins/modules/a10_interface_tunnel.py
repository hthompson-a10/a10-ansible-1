#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = r'''
module: a10_interface_tunnel
description:
    - Tunnel interface
short_description: Configures A10 interface.tunnel
author: A10 Networks 2018 
version_added: 2.4
options:
    state:
        description:
        - State of the object to be created.
        choices:
          - noop
          - present
          - absent
        required: True
    ansible_host:
        description:
        - Host for AXAPI authentication
        required: True
    ansible_username:
        description:
        - Username for AXAPI authentication
        required: True
    ansible_password:
        description:
        - Password for AXAPI authentication
        required: True
    ansible_port:
        description:
        - Port for AXAPI authentication
        required: True
    a10_device_context_id:
        description:
        - Device ID for aVCS configuration
        choices: [1-8]
        required: False
    a10_partition:
        description:
        - Destination/target partition for object/command
        required: False
    oper:
        description:
        - "Field oper"
        required: False
        suboptions:
            config_speed:
                description:
                - "Field config_speed"
            ipv6_list:
                description:
                - "Field ipv6_list"
            ipv4_netmask:
                description:
                - "IPv4 subnet mask"
            ipv6_link_local:
                description:
                - "Field ipv6_link_local"
            link_type:
                description:
                - "Field link_type"
            ipv4_addr_count:
                description:
                - "Field ipv4_addr_count"
            ipv4_list:
                description:
                - "Field ipv4_list"
            mac:
                description:
                - "Field mac"
            ifnum:
                description:
                - "Tunnel interface number"
            state:
                description:
                - "Field state"
            ipv6_link_local_type:
                description:
                - "Field ipv6_link_local_type"
            ipv6_link_local_scope:
                description:
                - "Field ipv6_link_local_scope"
            ipv6_addr_count:
                description:
                - "Field ipv6_addr_count"
            line_protocol:
                description:
                - "Field line_protocol"
            ipv6_link_local_prefix:
                description:
                - "Field ipv6_link_local_prefix"
            ipv4_address:
                description:
                - "IPv4 address"
    stats:
        description:
        - "Field stats"
        required: False
        suboptions:
            num_tx_err_pkts:
                description:
                - "sent error packets"
            rate_pkt_rcvd:
                description:
                - "Packet received rate packets/sec"
            num_rx_err_pkts:
                description:
                - "received error packets"
            ifnum:
                description:
                - "Tunnel interface number"
            num_total_rx_bytes:
                description:
                - "received bytes"
            rate_byte_sent:
                description:
                - "Byte sent rate bits/sec"
            rate_byte_rcvd:
                description:
                - "Byte received rate bits/sec"
            num_total_tx_bytes:
                description:
                - "sent bytes"
            num_tx_pkts:
                description:
                - "sent packets"
            rate_pkt_sent:
                description:
                - "Packet sent rate packets/sec"
            num_rx_pkts:
                description:
                - "received packets"
    name:
        description:
        - "Name for the interface"
        required: False
    ip:
        description:
        - "Field ip"
        required: False
        suboptions:
            uuid:
                description:
                - "uuid of the object"
            generate_membership_query:
                description:
                - "Enable Membership Query"
            rip:
                description:
                - "Field rip"
            max_resp_time:
                description:
                - "Max Response Time (Default is 100)"
            address:
                description:
                - "Field address"
            ospf:
                description:
                - "Field ospf"
            generate_membership_query_val:
                description:
                - "1 - 255 (Default is 125)"
    ifnum:
        description:
        - "Tunnel interface number"
        required: True
    user_tag:
        description:
        - "Customized tag"
        required: False
    mtu:
        description:
        - "Interface mtu (Interface MTU, default 1 (min MTU is 1280 for IPv6))"
        required: False
    sampling_enable:
        description:
        - "Field sampling_enable"
        required: False
        suboptions:
            counters1:
                description:
                - "'all'= all; 'num-rx-pkts'= received packets; 'num-total-rx-bytes'= received bytes; 'num-tx-pkts'= sent packets; 'num-total-tx-bytes'= sent bytes; 'num-rx-err-pkts'= received error packets; 'num-tx-err-pkts'= sent error packets; 'rate_pkt_sent'= Packet sent rate packets/sec; 'rate_byte_sent'= Byte sent rate bits/sec; 'rate_pkt_rcvd'= Packet received rate packets/sec; 'rate_byte_rcvd'= Byte received rate bits/sec; "
    load_interval:
        description:
        - "Configure Load Interval (Seconds (5-300, Multiple of 5), default 300)"
        required: False
    ipv6:
        description:
        - "Field ipv6"
        required: False
        suboptions:
            router:
                description:
                - "Field router"
            address_cfg:
                description:
                - "Field address_cfg"
            ospf:
                description:
                - "Field ospf"
            ipv6_enable:
                description:
                - "Enable IPv6 processing"
            uuid:
                description:
                - "uuid of the object"
    action:
        description:
        - "'enable'= Enable; 'disable'= Disable; "
        required: False
    speed:
        description:
        - "Speed in Gbit/Sec (Default 10 Gbps)"
        required: False
    uuid:
        description:
        - "uuid of the object"
        required: False


'''

EXAMPLES = """
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["action","ifnum","ip","ipv6","load_interval","mtu","name","oper","sampling_enable","speed","stats","user_tag","uuid",]

# our imports go at the top so we fail fast.
try:
    from ansible_collections.a10.acos_axapi.plugins.module_utils import errors as a10_ex
    from ansible_collections.a10.acos_axapi.plugins.module_utils.axapi_http import client_factory, session_factory
    from ansible_collections.a10.acos_axapi.plugins.module_utils.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist

except (ImportError) as ex:
    module.fail_json(msg="Import Error:{0}".format(ex))
except (Exception) as ex:
    module.fail_json(msg="General Exception in Ansible module import:{0}".format(ex))


def get_default_argspec():
    return dict(
        ansible_host=dict(type='str', required=True),
        ansible_username=dict(type='str', required=True),
        ansible_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default="present", choices=['noop', 'present', 'absent']),
        ansible_port=dict(type='int', choices=[80, 443], required=True),
        a10_partition=dict(type='dict', name=dict(type='str',), shared=dict(type='str',), required=False, ),
        a10_device_context_id=dict(type='int', choices=[1, 2, 3, 4, 5, 6, 7, 8], required=False, ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )

def get_argspec():
    rv = get_default_argspec()
    rv.update(dict(
        oper=dict(type='dict', config_speed=dict(type='int', ), ipv6_list=dict(type='list', is_anycast=dict(type='int', ), prefix=dict(type='str', ), addr=dict(type='str', )), ipv4_netmask=dict(type='str', ), ipv6_link_local=dict(type='str', ), link_type=dict(type='str', ), ipv4_addr_count=dict(type='int', ), ipv4_list=dict(type='list', mask=dict(type='str', ), addr=dict(type='str', )), mac=dict(type='str', ), ifnum=dict(type='int', required=True, ), state=dict(type='str', choices=['up', 'disabled', 'down']), ipv6_link_local_type=dict(type='str', ), ipv6_link_local_scope=dict(type='str', ), ipv6_addr_count=dict(type='int', ), line_protocol=dict(type='str', choices=['up', 'down']), ipv6_link_local_prefix=dict(type='str', ), ipv4_address=dict(type='str', )),
        stats=dict(type='dict', num_tx_err_pkts=dict(type='str', ), rate_pkt_rcvd=dict(type='str', ), num_rx_err_pkts=dict(type='str', ), ifnum=dict(type='int', required=True, ), num_total_rx_bytes=dict(type='str', ), rate_byte_sent=dict(type='str', ), rate_byte_rcvd=dict(type='str', ), num_total_tx_bytes=dict(type='str', ), num_tx_pkts=dict(type='str', ), rate_pkt_sent=dict(type='str', ), num_rx_pkts=dict(type='str', )),
        name=dict(type='str', ),
        ip=dict(type='dict', uuid=dict(type='str', ), generate_membership_query=dict(type='bool', ), rip=dict(type='dict', receive_cfg=dict(type='dict', receive=dict(type='bool', ), version=dict(type='str', choices=['2'])), uuid=dict(type='str', ), receive_packet=dict(type='bool', ), split_horizon_cfg=dict(type='dict', state=dict(type='str', choices=['poisoned', 'disable', 'enable'])), authentication=dict(type='dict', key_chain=dict(type='dict', key_chain=dict(type='str', )), mode=dict(type='dict', mode=dict(type='str', choices=['md5', 'text'])), str=dict(type='dict', string=dict(type='str', ))), send_cfg=dict(type='dict', version=dict(type='str', choices=['2']), send=dict(type='bool', )), send_packet=dict(type='bool', )), max_resp_time=dict(type='int', ), address=dict(type='dict', ip_cfg=dict(type='list', ipv4_address=dict(type='str', ), ipv4_netmask=dict(type='str', ))), ospf=dict(type='dict', ospf_ip_list=dict(type='list', dead_interval=dict(type='int', ), authentication_key=dict(type='str', ), uuid=dict(type='str', ), mtu_ignore=dict(type='bool', ), transmit_delay=dict(type='int', ), value=dict(type='str', choices=['message-digest', 'null']), priority=dict(type='int', ), authentication=dict(type='bool', ), cost=dict(type='int', ), database_filter=dict(type='str', choices=['all']), hello_interval=dict(type='int', ), ip_addr=dict(type='str', required=True, ), retransmit_interval=dict(type='int', ), message_digest_cfg=dict(type='list', md5_value=dict(type='str', ), message_digest_key=dict(type='int', ), encrypted=dict(type='str', )), out=dict(type='bool', )), ospf_global=dict(type='dict', cost=dict(type='int', ), dead_interval=dict(type='int', ), authentication_key=dict(type='str', ), network=dict(type='dict', broadcast=dict(type='bool', ), point_to_multipoint=dict(type='bool', ), non_broadcast=dict(type='bool', ), point_to_point=dict(type='bool', ), p2mp_nbma=dict(type='bool', )), mtu_ignore=dict(type='bool', ), transmit_delay=dict(type='int', ), authentication_cfg=dict(type='dict', authentication=dict(type='bool', ), value=dict(type='str', choices=['message-digest', 'null'])), retransmit_interval=dict(type='int', ), bfd_cfg=dict(type='dict', disable=dict(type='bool', ), bfd=dict(type='bool', )), disable=dict(type='str', choices=['all']), hello_interval=dict(type='int', ), database_filter_cfg=dict(type='dict', database_filter=dict(type='str', choices=['all']), out=dict(type='bool', )), priority=dict(type='int', ), mtu=dict(type='int', ), message_digest_cfg=dict(type='list', message_digest_key=dict(type='int', ), md5=dict(type='dict', md5_value=dict(type='str', ), encrypted=dict(type='str', ))), uuid=dict(type='str', ))), generate_membership_query_val=dict(type='int', )),
        ifnum=dict(type='int', required=True, ),
        user_tag=dict(type='str', ),
        mtu=dict(type='int', ),
        sampling_enable=dict(type='list', counters1=dict(type='str', choices=['all', 'num-rx-pkts', 'num-total-rx-bytes', 'num-tx-pkts', 'num-total-tx-bytes', 'num-rx-err-pkts', 'num-tx-err-pkts', 'rate_pkt_sent', 'rate_byte_sent', 'rate_pkt_rcvd', 'rate_byte_rcvd'])),
        load_interval=dict(type='int', ),
        ipv6=dict(type='dict', router=dict(type='dict', ripng=dict(type='dict', uuid=dict(type='str', ), rip=dict(type='bool', )), ospf=dict(type='dict', area_list=dict(type='list', area_id_addr=dict(type='str', ), tag=dict(type='str', ), instance_id=dict(type='int', ), area_id_num=dict(type='int', )), uuid=dict(type='str', ))), address_cfg=dict(type='list', address_type=dict(type='str', choices=['anycast', 'link-local']), ipv6_addr=dict(type='str', )), ospf=dict(type='dict', uuid=dict(type='str', ), bfd=dict(type='bool', ), cost_cfg=dict(type='list', cost=dict(type='int', ), instance_id=dict(type='int', )), priority_cfg=dict(type='list', priority=dict(type='int', ), instance_id=dict(type='int', )), hello_interval_cfg=dict(type='list', hello_interval=dict(type='int', ), instance_id=dict(type='int', )), mtu_ignore_cfg=dict(type='list', mtu_ignore=dict(type='bool', ), instance_id=dict(type='int', )), retransmit_interval_cfg=dict(type='list', retransmit_interval=dict(type='int', ), instance_id=dict(type='int', )), disable=dict(type='bool', ), transmit_delay_cfg=dict(type='list', transmit_delay=dict(type='int', ), instance_id=dict(type='int', )), neighbor_cfg=dict(type='list', neighbor_priority=dict(type='int', ), neighbor_poll_interval=dict(type='int', ), neig_inst=dict(type='int', ), neighbor=dict(type='str', ), neighbor_cost=dict(type='int', )), network_list=dict(type='list', broadcast_type=dict(type='str', choices=['broadcast', 'non-broadcast', 'point-to-point', 'point-to-multipoint']), p2mp_nbma=dict(type='bool', ), network_instance_id=dict(type='int', )), dead_interval_cfg=dict(type='list', dead_interval=dict(type='int', ), instance_id=dict(type='int', ))), ipv6_enable=dict(type='bool', ), uuid=dict(type='str', )),
        action=dict(type='str', choices=['enable', 'disable']),
        speed=dict(type='int', ),
        uuid=dict(type='str', )
    ))
   

    return rv

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/interface/tunnel/{ifnum}"

    f_dict = {}
    f_dict["ifnum"] = module.params["ifnum"]

    return url_base.format(**f_dict)

def oper_url(module):
    """Return the URL for operational data of an existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/oper"

def stats_url(module):
    """Return the URL for statistical data of and existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/stats"

def list_url(module):
    """Return the URL for a list of resources"""
    ret = existing_url(module)
    return ret[0:ret.rfind('/')]

def get(module):
    return module.client.get(existing_url(module))

def get_list(module):
    return module.client.get(list_url(module))

def get_oper(module):
    if module.params.get("oper"):
        query_params = {}
        for k,v in module.params["oper"].items():
            query_params[k.replace('_', '-')] = v 
        return module.client.get(oper_url(module),
                                 params=query_params)
    return module.client.get(oper_url(module))

def get_stats(module):
    if module.params.get("stats"):
        query_params = {}
        for k,v in module.params["stats"].items():
            query_params[k.replace('_', '-')] = v
        return module.client.get(stats_url(module),
                                 params=query_params)
    return module.client.get(stats_url(module))

def exists(module):
    try:
        return get(module)
    except a10_ex.NotFound:
        return None

def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")

def _build_dict_from_param(param):
    rv = {}

    for k,v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        elif isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv

def build_envelope(title, data):
    return {
        title: data
    }

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/interface/tunnel/{ifnum}"

    f_dict = {}
    f_dict["ifnum"] = ""

    return url_base.format(**f_dict)

def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if x in params and params.get(x) is not None])
    
    errors = []
    marg = []
    
    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID
    
    if not rc:
        errors.append(msg.format(", ".join(marg)))
    
    return rc,errors

def build_json(title, module):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v is not None:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            elif isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)

def report_changes(module, result, existing_config, payload):
    if existing_config:
        for k, v in payload["tunnel"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
               break
            else:
                if existing_config["tunnel"][k] != v:
                    if result["changed"] != True:
                        result["changed"] = True
                    existing_config["tunnel"][k] = v
            result.update(**existing_config)
    else:
        result.update(**payload)
    return result

def create(module, result, payload):
    try:
        post_result = module.client.post(new_url(module), payload)
        if post_result:
            result.update(**post_result)
        result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def update(module, result, existing_config, payload):
    try:
        post_result = module.client.post(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def present(module, result, existing_config):
    payload = build_json("tunnel", module)
    changed_config = report_changes(module, result, existing_config, payload)
    if module.check_mode:
        return changed_config
    elif not existing_config:
        return create(module, result, payload)
    elif existing_config and not changed_config.get('changed'):
        return update(module, result, existing_config, payload)
    else:
        result["changed"] = True
        return result

def delete(module, result):
    try:
        module.client.delete(existing_url(module))
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def absent(module, result, existing_config):
    if module.check_mode:
        if existing_config:
            result["changed"] = True
            return result
        else:
            result["changed"] = False
            return result
    else:
        return delete(module, result)

def replace(module, result, existing_config, payload):
    try:
        post_result = module.client.put(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def run_command(module):
    run_errors = []

    result = dict(
        changed=False,
        original_message="",
        message="",
        result={}
    )

    state = module.params["state"]
    ansible_host = module.params["ansible_host"]
    ansible_username = module.params["ansible_username"]
    ansible_password = module.params["ansible_password"]
    ansible_port = module.params["ansible_port"]
    a10_partition = module.params["a10_partition"]
    a10_device_context_id = module.params["a10_device_context_id"]

    if ansible_port == 80:
        protocol = "http"
    elif ansible_port == 443:
        protocol = "https"

    valid = True

    if state == 'present':
        valid, validation_errors = validate(module.params)
        for ve in validation_errors:
            run_errors.append(ve)
    
    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(ansible_host, ansible_port, protocol, ansible_username, ansible_password)
    
    if a10_partition:
        module.client.activate_partition(a10_partition)

    if a10_device_context_id:
        module.client.change_context(a10_device_context_id)

    existing_config = exists(module)
    
    if state == 'present':
        result = present(module, result, existing_config)

    elif state == 'absent':
        result = absent(module, result, existing_config)
    
    elif state == 'noop':
        if module.params.get("get_type") == "single":
            result["result"] = get(module)
        elif module.params.get("get_type") == "list":
            result["result"] = get_list(module)
        elif module.params.get("get_type") == "oper":
            result["result"] = get_oper(module)
        elif module.params.get("get_type") == "stats":
            result["result"] = get_stats(module)
    module.client.session.close()
    return result

def main():
    module = AnsibleModule(argument_spec=get_argspec(), supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)

# standard ansible module imports
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()