

def R01_Existing_Masergy():
 print("""
config t
class-map match-any NC
 match access-group name BGP
class-map match-any CITRIX-CM
 match access-group name CITRIX-Masergy-ACL
!
policy-map MASERGY-Outbound
 class CITRIX-CM
  set dscp af31
 class NC
  set dscp cs7
!
interface {{{XXX}}}
service-policy output MASERGY-Outbound
!
no int {{{XXX}}}.100
no int {{{XXX}}}.200
!
interface {{{XXX}}}
no shutdown
description to Switch
ip address {{{XXX}}}
ip ospf network point-to-point
no ip redirects
no ip proxy-arp
media-type rj45
negotiation auto
ip flow monitor FlowMonitor input
ip flow monitor FlowMonitor output
!
router bgp {{{XXX}}}
bgp router-id {{{XXX}}}
{{{bgp redistribute-internal}}}
network {{{XXX}}} mask 255.255.255.252
!
no router ospf {{{XXX}}}
!
router ospf {{{XXX}}}
router-id {{{XXX}}}
passive-interface default
no passive-interface {{{XXX}}}
network 0.0.0.0 255.255.255.255 area 0
default-information originate metric 1 metric-type 1
{{{distance 201}}}
!
ip access-list extended BGP
 permit tcp any any eq bgp
 permit tcp any eq bgp any
ip access-list extended CITRIX-Masergy-ACL
 permit tcp any eq 1494 any
 permit tcp any any eq 1494
 permit tcp any eq 2598 any
 permit tcp any any eq 2598
!
no logging source-interface {{{XXX}}}.100
no snmp-server trap-source {{{XXX}}}.100
no snmp-server source-interface informs {{{XXX}}}.100
no ntp source {{{XXX}}}.100
!
""")