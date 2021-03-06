#!/usr/bin/env python
#
# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Encode configuration for model Cisco-IOS-XR-clns-isis-cfg.

usage: cd-encode-xr-clns-isis-cfg-55-ydk.py [-h] [-v]

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
"""

from argparse import ArgumentParser
from urlparse import urlparse

from ydk.services import CodecService
from ydk.providers import CodecServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_clns_isis_cfg \
    as xr_clns_isis_cfg
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_clns_isis_datatypes \
    as xr_clns_isis_datatypes
from ydk.types import Empty
import logging


def config_isis(isis):
    """Add config data to isis object."""
    # global configuration
    instance = isis.instances.Instance()
    instance.instance_name = "DEFAULT"
    instance.running = Empty()
    instance.is_type = xr_clns_isis_cfg.IsisConfigurableLevelsEnum.level1
    net = instance.nets.Net()
    net.net_name = "49.0000.1720.1625.5001.00"
    instance.nets.net.append(net)
    isis.instances.instance.append(instance)
    # global address family
    af = instance.afs.Af()
    af.af_name = xr_clns_isis_datatypes.IsisAddressFamilyEnum.ipv6
    af.saf_name = xr_clns_isis_datatypes.IsisSubAddressFamilyEnum.unicast
    af.af_data = af.AfData()
    metric_style = af.af_data.metric_styles.MetricStyle()
    metric_style.style = xr_clns_isis_cfg.IsisMetricStyleEnum.new_metric_style
    metric_style.level = xr_clns_isis_datatypes.IsisInternalLevelEnum.not_set
    transition_state = xr_clns_isis_cfg.IsisMetricStyleTransitionEnum.disabled
    metric_style.transition_state = transition_state
    af.af_data.metric_styles.metric_style.append(metric_style)
    # segment routing
    mpls = xr_clns_isis_cfg.IsisLabelPreferenceEnum.LDP
    af.af_data.segment_routing.mpls = mpls
    instance.afs.af.append(af)

    # loopback interface
    interface = instance.interfaces.Interface()
    interface.interface_name = "Loopback0"
    interface.running = Empty()
    interface.state = xr_clns_isis_cfg.IsisInterfaceStateEnum.passive
    # interface address family
    interface_af = interface.interface_afs.InterfaceAf()
    interface_af.af_name = xr_clns_isis_datatypes.IsisAddressFamilyEnum.ipv6
    interface_af.saf_name = xr_clns_isis_datatypes.IsisSubAddressFamilyEnum.unicast
    interface_af.interface_af_data.running = Empty()
    interface.interface_afs.interface_af.append(interface_af)
    # segment routing
    prefix_sid = interface_af.interface_af_data.PrefixSid()
    prefix_sid.type = xr_clns_isis_cfg.IsissidEnum.absolute
    prefix_sid.value = 16061
    prefix_sid.php = xr_clns_isis_cfg.IsisphpFlagEnum.enable
    explicit_null = xr_clns_isis_cfg.IsisexplicitNullFlagEnum.disable
    prefix_sid.explicit_null = explicit_null
    prefix_sid.nflag_clear = xr_clns_isis_cfg.NflagClearEnum.disable
    interface_af.interface_af_data.prefix_sid = prefix_sid
    instance.interfaces.interface.append(interface)

    # gi0/0/0/0 interface
    interface = instance.interfaces.Interface()
    interface.interface_name = "GigabitEthernet0/0/0/0"
    interface.running = Empty()
    interface.point_to_point = Empty()
    # interface address familiy
    interface_af = interface.interface_afs.InterfaceAf()
    interface_af.af_name = xr_clns_isis_datatypes.IsisAddressFamilyEnum.ipv6
    interface_af.saf_name = xr_clns_isis_datatypes.IsisSubAddressFamilyEnum.unicast
    interface_af.interface_af_data.running = Empty()
    interface.interface_afs.interface_af.append(interface_af)
    instance.interfaces.interface.append(interface)


if __name__ == "__main__":
    """Execute main program."""
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")
    args = parser.parse_args()

    # log debug messages if verbose argument specified
    if args.verbose:
        logger = logging.getLogger("ydk")
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(("%(asctime)s - %(name)s - "
                                      "%(levelname)s - %(message)s"))
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # create codec provider
    provider = CodecServiceProvider(type="xml")

    # create codec service
    codec = CodecService()

    isis = xr_clns_isis_cfg.Isis()  # create object
    config_isis(isis)  # add object configuration

    # encode and print object
    print(codec.encode(provider, isis))

    provider.close()
    exit()
# End of script
