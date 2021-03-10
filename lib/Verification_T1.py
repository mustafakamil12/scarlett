# -- Site Verification T1--

import os
from datetime import datetime
from lib.MB_Parent import *
from lib.Scarlett_Logo import *

def Verification_Test_T1 (MB, PON, ESR, Site, Port, Carrier,  CKT_ID, Serial, POPID):
 
 dt = datetime.now()
 Test_date =  '{:%B %d %Y}'.format(dt)
 Test_time_hour = '{:%I }'.format(dt)
 Test_time_min = '{:%M %p}'.format(dt)
 
 ManageGW = input ("GW from IPARMS: ")
 ManageIP = input ("IP from IPARMS: ")
 
 print ("\nfind a good CAS name: /opt/t2/bin/easyname %s" %ManageIP)
 CAS = input("CAS Name: ")
 os.system('cls')
 Logo_printer()
 
 print ( "\n\nSite Verification Start at: %s %s: %s cst" % (Test_date, Test_time_hour, Test_time_min))
 
 print("""\nSite Verification Information:-
-------------------------
  \n """ )
  
 print ("1. Bundle ID: %s" % MB)                #The sequence number need to be checked..!
 print ("2. PON Number: %s" % PON)
 print ("3. ESR : %s" % ESR)
 print ("4. Site Address: %s" % Site)
 print ("5. Port #: %s" % Port)
 print ("6. Carrier Name: %s" % Carrier)
 print ("7. Circuit ID: %s" % CKT_ID)
 print ("8. Serial No.: %s" %Serial)
 print ("9. Step had been made\n\n")
 print ("Configuration Section:-\n")
 print (""" clock-source node-timed
                channel-group 1
                    description "PON %s"
                    encap-type bcp-dot1q
                    timeslots 1-24
                    no shutdown
                exit
		no shutdown \n""" % PON)	
				
 
 
 
 print ("""\nOverture ISG-140 MIB:
Device Number: %s
Serial Number: %s
Bundle ID for Serial link: %s
Management IP Address: %s
GW:  %s""" %(CAS, Serial, MB, ManageIP, ManageGW))
 print("---------------------------------------------")
 print("configure service vpls 1688093")
 print (""" sap %s.1:93 create


After configure VPLS 1688093 put lines below ASAP:-

                auto-learn-mac-protect
                restrict-protected-src 
                ingress
                    qos 3
                exit
                egress
                    qos 3
                exit""" %Port)
				
				
 print ("""----------------------------------------------------
ESS2.%s admin  j@y!,!32
----------------------------------------------------

Default Overture Creds: admin/masergy at this point we need to change the password

----------------------------------------------------

Check the statistics for this CKT.                  =================> CPE Configuration Complete

----------------------------------------------------

From ESR use This:-

ping %s router 2705 count 10000 size 1472 rapid    ================> Site Verification Complete
as example below


A:%s# ping %s router 2705 count 1000 rapid """ %(POPID, ManageIP, ESR, ManageIP))
 return