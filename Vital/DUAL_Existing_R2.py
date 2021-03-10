


def DUAL_Existing_R2():
 print("""
config t
!
track 10 ip route 10.130.0.0/16 reachability
!
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
default interface {{{XXX}}}
!
interface {{{XXX}}}
description Masergy Circuit ID: {{{XXX}}}
ip address {{{XXX}}} 255.255.255.252
no ip redirects
no ip proxy-arp
ip flow monitor FlowMonitor input
ip flow monitor FlowMonitor output
no shutdown
service-policy output MASERGY-Outbound
!
!
!
no router bgp {{{XXX}}}
!
router bgp {{{XXX}}}
bgp router-id {{{XXX}}}
bgp log-neighbor-changes
neighbor {{{XXX}}} remote-as {{{XXX}}}
neighbor {{{XXX}}} description iBGP to Masergy FG
neighbor {{{XXX}}} send-community
neighbor {{{XXX}}} next-hop-self
neighbor {{{XXX}}} route-map LOC-PREF-COMMUNITY out
neighbor {{{XXX}}} soft-reconfiguration inbound
network {{{XXX}}} mask {{{XXX}}} 
network {{{XXX}}} mask {{{XXX}}} 
network {{{XXX}}} mask 255.255.255.252
network {{{XXX}}} mask 255.255.255.252
{{{ bgp redistribute-internal}}}
!
!
!
ip bgp-community new-format
!
ip prefix-list LOC-PREF-COMMUNITY permit {{{XXX}}}
ip prefix-list LOC-PREF-COMMUNITY permit {{{XXX}}}
!
!
route-map LOC-PREF-COMMUNITY permit 10
match ip address prefix-list LOC-PREF-COMMUNITY
set community 19855:70
!
route-map LOC-PREF-COMMUNITY permit 20
!
router ospf {{{XXX}}}
router-id {{{XXX}}}
{{{Distance 201}}}
default-information originate metric 200 metric-type 1
!
no logging source-interface {{{XXX}}}
no snmp-server trap-source {{{XXX}}}
no snmp-server source-interface informs {{{XXX}}}
no ntp source {{{XXX}}}
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
""")