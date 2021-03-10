# -- Site Verification 114 --

import os
from datetime import datetime
from lib.MB_Parent import *
from lib.Port_Rec import *
from lib.Scarlett_Logo import *

def Verification_Test_114 (MB, PON, ESR, Site, Port, Carrier,  CKT_ID, Serial, STAG):
 dt = datetime.now()
 Test_date =  '{:%B %d %Y}'.format(dt)
 Test_time_hour = '{:%I }'.format(dt)
 Test_time_min = '{:%M %p}'.format(dt)
 

 PortList = Port_Rcog(Port,STAG) 
 ManageGW = input ("GW from IPARMS: ")
 ManageIP = input ("IP from IPARMS: ")
 
 print ("\nfind a good CAS name: /opt/t2/bin/easyname %s" %ManageIP)
 CAS = input("CAS Name: ")
 os.system('cls')
 Logo_printer()
 print ( "\n\nSite Verification Start at: %s %s: %s cst\n" % (Test_date, Test_time_hour, Test_time_min))
 
 print("""\nSite Verification Information:-
-------------------------
  \n """ )
  
 print ("1. Bundle ID: %s" % MB)                #The sequence number need to be checked..!
 print ("2. PON Number: %s" % PON)
 print ("3. ESR : %s" % ESR)
 print ("4. Site Address: %s" % Site)
 print ("5. Port #: %s.%s" % (Port,STAG))
 print ("6. Carrier Name: %s" % Carrier)
 print ("7. Circuit ID: %s" % CKT_ID)
 print ("8. Serial No.: %s" %Serial)
 				
 
 
 
 print ("""\nADVA  114 MIB:
Device Number: %s
Serial Number: %s
Bundle ID for Serial link: %s
Management IP Address: %s
GW:  %s""" %(CAS, Serial, MB, ManageIP, ManageGW))
 
 print ("\n***** CPE configuration complete *******\n")
 print("=============================================")
 print("\nconfigure service vprn 99999")
 print ("""\n


%s# configure service vprn 99999

Now Create VLAN 93

interface “MMR”  ======> MGMT IP subnet must be here
info
sap %s create

 \n""" %(ESR, PortList))
				
 print ("----------------------------------------------------\n")				
 
 print ("""Ping ADVA

%s# ping router 99999 192.168.2.2

Telnet to ADVA

%s# telnet router 99999 192.168.2.2\n""" %(ESR, ESR))
 
 print ("----------------------------------------------------\n")
 print("""Changing Default IP

ADVA# configure communication
		configure mgmttnl mgmt_tnl-1
		ip-address %s 255.255.252.0 %s
		(be careful because you will now lose access the ADVA)


Log again cause u will lost the access.

%s# telnet router 99999 %s""" %(ManageIP, ManageGW, ESR, ManageIP))
 
 print ("----------------------------------------------------\n")
 
 print ("""Remove VLAN 93

%s# configure service vprn 99999
interface “MMR”
sap %s shutdown 
no sap %s """ %(ESR, PortList, PortList))
 
 print ("\n----------------------------------------------------\n") 
 
 print("""Add VLAN 93 to VPLS 1688093

%s# configure service vpls 1688093
	   sap %s create 
                
Do the below part ASAP...

                auto-learn-mac-protect
                restrict-protected-src 
                ingress
                    qos 3
                exit
                egress
                    qos 3
                exit\n""" %(ESR, PortList))
 
 print ("\n----------------------------------------------------\n")
 print("Ping The permenant IP from NOC server")
 print ("\n----------------------------------------------------\n")
 print("Generate the Script from the NOC srver. generatescript.pl")
 print ("\n----------------------------------------------------\n")
 print ("Test Result\n\n")
 print("=============================================")
 print ("\n***** Site Verification complete *******")
 
 return