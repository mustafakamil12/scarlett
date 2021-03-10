


def DUAL_Switch_New_Configuration_24PS():

 print ("""
service timestamps debug datetime msec localtime show-timezone
service timestamps log datetime msec localtime show-timezone
service password-encryption
service compress-config
!
hostname {{{XXX}}}
!
boot-start-marker
boot-end-marker
!
!
logging buffered 32000
enable secret {{{XXX}}}#W0rldCup2052
!
username admin secret {{{XXX}}}#W0rldCup2052
username vital secret G0Fly3rs!
username masergy secret M@53rgy-N0C!@#$
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
{{{clock timezone PST -8 0}}}
{{{clock summer-time PST recurring}}}
{{{switch 1 provision ws-c3650-48ps}}}
ip routing
!
no ip domain-lookup
ip domain-name hubinternational.com
!
!
vtp domain none
vtp mode transparent
udld enable
!
!
!
!
!
diagnostic bootup level minimal
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
spanning-tree vlan 1-3999 priority 24576
!
redundancy
 mode sso
!
!
vlan 100
 name Data
!
vlan 200
 name Voice
!
vlan 999
 name stub-vlan
!
ip ssh version 2
!
!
!
!
!
!
!
interface range GigabitEthernet1/0/1-19
 switchport access vlan 100
 switchport mode access
 switchport voice vlan 200
 storm-control broadcast level 75.00
 storm-control multicast level 75.00
 nmsp attachment suppress
 spanning-tree portfast
 no shutdown
!
interface GigabitEthernet1/0/20
description ** UPS **
 switchport access vlan 100
 switchport mode access
 storm-control broadcast level 75.00
 storm-control multicast level 75.00
 nmsp attachment suppress
 spanning-tree portfast
 no shutdown
!
interface range GigabitEthernet1/0/21-23
 switchport access vlan 100
 switchport mode access
 switchport voice vlan 200
 storm-control broadcast level 75.00
 storm-control multicast level 75.00
 nmsp attachment suppress
 spanning-tree portfast
 no shutdown
!
interface Gi1/0/24
no switchport
description To Masergy R01
no shutdown
ip address {{{XXX}}}
ip ospf network point-to-point
!
interface Vlan100
 ip address {{{XXX}}}
 ip helper-address 10.130.67.12
 ip helper-address 10.125.3.12
 ip helper-address 10.30.32.123
 ip helper-address 10.130.67.4
 no ip redirects
 no ip proxy-arp
 no shutdown
!
interface Vlan200
 ip address {{{XXX}}}
 ip helper-address 10.130.67.12
 ip helper-address 10.125.3.12
 ip helper-address 10.30.32.123
 ip helper-address 10.130.67.4
 no ip redirects
 no ip proxy-arp
 no shutdown
!
{{{XXX
router ospf 1
router-id {{{XXX}}}
passive-interface default
no passive-interface {{{XXX}}}
no passive-interface {{{XXX}}}
network 0.0.0.0 255.255.255.255 area 0
XXX}}}
!
{{{XXX
ip route 0.0.0.0 0.0.0.0 {{{XXX}}}
ip default-gateway {{{XXX}}}
XXX}}}
!
no ip http server
no ip http authentication
no ip http secure-server
!
!
logging trap warnings
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
snmp-server community v!tal-n3tw0rK-N5 RO 6
snmp-server community HUB908#451$ RO 6
snmp-server trap-source Vlan100
snmp-server source-interface informs Vlan100
snmp-server location {{{XXXX}}}
snmp-server contact HUB_IT_Operations_Networks@hubinternational.com
snmp-server system-shutdown
snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart
snmp-server enable traps vtp
snmp-server enable traps vlancreate
snmp-server enable traps vlandelete
snmp-server enable traps envmon fan shutdown supply temperature status
snmp-server enable traps port-security
snmp-server enable traps config
snmp-server enable traps bridge newroot topologychange
snmp-server enable traps vlan-membership
snmp-server host 10.131.10.4 informs version 2c v!tal-n3tw0rK-N5  config
snmp-server host 10.130.16.125 version 2c HUB908#451$ 
snmp-server host 10.130.16.235 version 2c HUB908#451$ 
snmp-server host 10.130.16.56 version 2c HUB908#451$ 
snmp-server host 10.130.43.1 version 2c HUB908#451$ 
snmp ifmib ifindex persist
!
!
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
 exec-timeout 15 0
line vty 0 15
 login authentication local_auth
 transport input ssh
 exec-timeout 15 0
!
ntp source Vlan100
ntp server 10.130.30.20
ntp server 10.130.16.70
!
crypto key gen rsa mod 1024

""")