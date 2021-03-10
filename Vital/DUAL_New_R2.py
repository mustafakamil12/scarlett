

def DUAL_New_R2():
 print ("""
no service pad
service tcp-keepalives-in
service tcp-keepalives-out
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
no platform punt-keepalive disable-kernel-core
platform qos marker-statistics
!
hostname {{{XXX}}}
!
boot-start-marker
boot-end-marker
!
!
!
enable secret {{{XXX}}}#W0rldCup2052
!
aaa new-model
!
!
aaa authentication login local_auth local
!
!
!
!
!
!
aaa session-id common
{{{clock timezone EST -5 0}}}
{{{clock summer-time EST recurring}}}
!
!
!
!
!
!
track 10 ip route 10.130.0.0/16 reachability
!
!
!
!
!
!
ip name-server 10.4.48.10
no ip domain lookup
ip domain name hubinternational.com
!
!
!
!
!
!
!
!
!
!
subscriber templating
!
!
flow record FlowRecorder
 match ipv4 tos
 match ipv4 protocol
 match ipv4 source address
 match ipv4 destination address
 match transport source-port
 match transport destination-port
 match interface input
 match flow direction
 collect routing source as
 collect routing destination as
 collect routing next-hop address ipv4
 collect ipv4 dscp
 collect ipv4 id
 collect ipv4 source prefix
 collect ipv4 source mask
 collect ipv4 destination mask
 collect transport tcp flags
 collect interface output
 collect flow sampler
 collect counter bytes
 collect counter packets
 collect timestamp sys-uptime first
 collect timestamp sys-uptime last
 collect application name
!
!
flow exporter FlowExporter
 destination 10.131.10.3
 source Gi0/0/0
 transport udp 2055
 option interface-table
 option application-table
 option application-attributes
!
!
flow monitor FlowMonitor
 exporter FlowExporter
 cache timeout inactive 10
 cache timeout active 60
 record FlowRecorder
!
!
!
!
!
!
username admin secret 0 {{{XXX}}}#W0rldCup2052
username vital secret 0 G0Fly3rs!
username masergy secret M@53rgy-N0C!@#$
!
redundancy
 mode none
!
!
!
!
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
!
!
!
!
! 
!
!
!
!
!
!
!
!
!
!
! 
! 
! 
! 
! 
! 
!
!
interface GigabitEthernet0/0/0
description Masergy Circuit ID: {{{XXX}}}
ip address {{{XXX}}}
no ip redirects
no ip proxy-arp
media-type rj45
negotiation auto
ip flow monitor FlowMonitor input
ip flow monitor FlowMonitor output
no shutdown
service-policy output MASERGY-Outbound
!
interface Gi0/0/1
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
!
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
router ospf 1
router-id {{{XXX}}} 
network 0.0.0.0 255.255.255.255 area 0
passive-interface default
no passive-interface Gi0/0/1
{{{Distance 201}}}
default-information originate metric 200 metric-type 1
!
ip forward-protocol nd
no ip http server
no ip http secure-server
ip ssh version 2
ip scp server enable
!
ip bgp-community new-format
!
ip prefix-list LOC-PREF-COMMUNITY permit {{{XXX}}}
ip prefix-list LOC-PREF-COMMUNITY permit {{{XXX}}}
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
!
no service-routing capabilities-manager
logging buffered 32000
logging history size 20
logging history notifications
logging trap warnings
logging source-interface Gi0/0/1
logging host 10.130.16.125
logging host 10.130.16.235
logging host 10.130.43.1
access-list 6 permit 10.131.10.131
access-list 6 permit 10.131.10.130
access-list 6 permit 10.131.10.132
access-list 6 permit 10.130.28.249
access-list 6 permit 10.130.16.235
access-list 6 permit 10.131.10.3
access-list 6 permit 10.131.10.2
access-list 6 permit 10.131.10.4
access-list 6 permit 10.130.16.56
access-list 6 permit 10.130.43.1
access-list 6 permit 10.130.16.125
!
route-map LOC-PREF-COMMUNITY permit 10
match ip address prefix-list LOC-PREF-COMMUNITY
set community 19855:70
!
route-map LOC-PREF-COMMUNITY permit 20
!
snmp-server community v!tal-n3tw0rK-N5 RO 6
snmp-server community HUB908#451$ RO 6
snmp-server trap-source Gi0/0/1
snmp-server source-interface informs Gi0/0/1
snmp-server location {{{XXX}}}
snmp-server contact HUB_IT_Operations_Networks@hubinternational.com
snmp-server enable traps config
snmp-server host 10.131.10.4 informs version 2c v!tal-n3tw0rK-N5  config
snmp-server host 10.130.16.125 version 2c HUB908#451$ 
snmp-server host 10.130.16.235 version 2c HUB908#451$ 
snmp-server host 10.130.16.56 version 2c HUB908#451$ 
snmp ifmib ifindex persist
!
!
!
!
control-plane
!
banner login ^
********************************************************************************
* WARNING UNAUTHORIZED ACCESS IS PROHIBITED                                    *
*                                                                              *
* SECURITY & PRIVACY DISCLAIMER                                                *
*                                                                              *
* This system is restricted solely to authorized users for legitimate business *
* purposes only. The actual or attempted unauthorized access, use or           *
* modification of this system is strictly prohibited,is unlawful, and may be   *
* subject to civil and/or criminal penalties. Any use of the system may be     *
* logged or monitored without further notice, and that the resulting logs may  *
* be used as evidence in court.                                                *
*                                                                              *
* HUB INTERNATIONAL INC. AND ITS SUBSIDIARIES                                  *
********************************************************************************
^
!
line con 0
 login authentication local_auth
exec-timeout 15 0
line aux 0
 login authentication local_auth
stopbits 1
exec-timeout 15 0
line vty 0 15
 login authentication local_auth
exec-timeout 15 0
transport input ssh
!
ntp source gi0/0/1
ntp server 10.130.30.20
ntp server 10.130.16.70
!
crypto key gen rsa mod 1024

""")