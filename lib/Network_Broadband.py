#Network Configuration for Broadband...

import os
from datetime import datetime
from lib.MB_Parent import *
from netaddr import *
from lib.Scarlett_Logo import *

def NETWORK_Config_Broadband (MB, PON, ESR, Site, Port, Carrier,  CKT_ID,  POP, Serial, MTEPublic, MTEGW, UPload, LanIP, ESRVTI, MTEVTI, AS):
 dt = datetime.now()
 Test_date =  '{:%B %d %Y}'.format(dt)
 Test_time_hour = '{:%I }'.format(dt)
 Test_time_min = '{:%M %p}'.format(dt)
 _Prep_tkt = input("Prep TKT: ")

 os.system('cls')
 Logo_printer()
 print ( "\n\nNetwork Configuration Start at: %s %s: %s cst" % (Test_date, Test_time_hour, Test_time_min))

 print("""\nNetwork Configuration Information:-
-------------------------
  \n """ )

 print ("1. Site Address: %s" % Site)
 print ("2. Bundle ID: %s" % MB)                #The sequence number need to be checked..!
 print ("3. PON Number: %s" % PON)
 print ("4. Carrier Name: %s" % Carrier)
 print ("5. Circuit ID: %s" % CKT_ID)


 print("7. Prep TKT: %s" %_Prep_tkt)

 print("""\n8. Steps had been Made:

***** Circuit Comments Box: WORKING ON NETWORK CONFIGURATIONS  ******

9. Notes:-

 /data/noctools/bin/t2_makenotes %s



\n""" %MB)

 xIP = IPNetwork(MTEPublic)
 Subnet_ID = xIP[0]

 ESR_Public_IP_Address = input("ESR Public IP Address: ")

 print("""\n10. TCIF information:-

NaaS Termination Device: %s
MTE Public IP Address: %s	   ===> Subnet ID: %s
ESR Public IP Address: %s
Gateway: %s \n""" %(POP, MTEPublic, Subnet_ID, ESR_Public_IP_Address, MTEGW))




 print ("""NaaS 2.0 Encryption:	aes128-sha1
ESR VTI IP Address: %s
MTE VTI IP Address:	%s
MTE VTI BGP ASN: %s""" % (ESRVTI, MTEVTI, AS))


 LanIP = ''.join(LanIP.split())

 if LanIP  :
  #print("There's text in this variable")
  yIP = IPNetwork(LanIP)     #Need to put something for empty information...
  _MTE_LAN_subnet = yIP[0]
  _MTE_LAN_IP_Neighbor = yIP[2]
  #print("LAN IP: %s, LAN Neighbor IP: %s" %(_MTE_LAN_subnet, _MTE_LAN_IP_Neighbor))

 elif not LanIP :
  print ("\nThere's No LAN IP\n")
  _MTE_LAN_subnet = ""
  _MTE_LAN_IP_Neighbor = ""



 print("""\nMTE LAN IP Address:	%s
MTE LAN IP Neighbor: %s
MTE LAN subnet: %s""" %(LanIP, _MTE_LAN_IP_Neighbor, _MTE_LAN_subnet))

 _Device = input("\nEnter Device Number from the NEMS: ")
 _VPRN = input ("Enter VPRN: ")


 print ("""\n13) MTE Information:-

FortiGate 60D:
Hostname: MTE%s-%s
Chassis Serial Number: %s
Bundle ID for Loopback IP:%s
WAN1 IP Address:  %s
LAN IP Address:   %s
VPRN: %s""" %(_Device, POP, Serial, MB, MTEPublic, LanIP, _VPRN))

 print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

 print("\nVlan: \n")
 print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
 print("Configuration:- \n\n")
