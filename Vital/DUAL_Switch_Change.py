

def DUAL_Switch_Change():
 print("""
config t
default interface {{{XXX}}}
default interface {{{XXX}}}
!
interface {{{XXX}}}
no switchport
description To Masergy R01
no shutdown
ip address {{{XXX}}}
ip ospf network point-to-point
!
interface {{{XXX}}}
no switchport
description To Masergy R02
no shutdown
ip address {{{XXX}}}
ip ospf network point-to-point
!
interface range XX/XX-XX {{{Only applicable on C3560s not C3650s}}}
no srr-queue {{{XXX}}}
no srr-queue {{{XXX}}}
no mls qus vlan-based
no priority-queue out
mls qos trust dscp
!
interface range XX/XX-XX {{{Only applicable on C3650s not C3560s}}}
no service-policy output 3650-Output-Policy
!
!
router ospf {{{XXX}}}
router-id {{{XXX}}}
passive-interface default
no passive-interface {{{XXX}}}
no passive-interface {{{XXX}}}
network 0.0.0.0 255.255.255.255 area 0
!
interface Vlan100
no service-policy input {{{XXX}}}
!
interface Vlan200
no service-policy input {{{XXX}}}
!
""")