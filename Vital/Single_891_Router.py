

def Single_891_R():

 print("""\nSingle-891-Router-Change
------------------------\n
config t
default interface {{{XXX}}}
!
interface {{{XXX}}}
description Masergy Circuit ID: {{{XXX}}}
ip address {{{XXX}}} 255.255.255.252
ip flow monitor FlowMonitor input
ip flow monitor FlowMonitor output
ip flow ingress
ip flow egress
duplex auto
speed auto
no shutdown
!
interface Vlan100
no crypto ipsec client ezvpn HUBEZVPN inside
!
interface Vlan200
no crypto ipsec client ezvpn HUBEZVPN inside
!
track 10 ip route 0.0.0.0/0 reachability
!
router bgp {{{XXX}}}
bgp log-neighbor-changes
bgp router-id {{{XXX}}}
network {{{XXX}}} mask 255.255.255.0
network {{{XXX}}} mask 255.255.255.0
network {{{XXX}}} mask 255.255.255.252
neighbor {{{XXX}}} remote-as {{{XXX}}}
neighbor {{{XXX}}} next-hop-self
neighbor {{{XXX}}} description iBGP to Masergy FG
neighbor {{{XXX}}} send-community
neighbor {{{XXX}}} soft-reconfiguration inbound
!
ip bgp-community new-format
!
""")