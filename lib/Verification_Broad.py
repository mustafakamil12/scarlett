# -- Planet Test --

import os
from datetime import datetime
from lib.MB_Parent import *
from lib.Scarlett_Logo import *

def Site_Verification_Broad (MB, PON, ESR, Site, GW, Carrier, CKT_ID, Serial, POP, MTEPublic):
 dt = datetime.now()
 Test_date =  '{:%B %d %Y}'.format(dt)
 Test_time_hour = '{:%I }'.format(dt)
 Test_time_min = '{:%M %p}'.format(dt)
 
 _Firm_Version = input	("Could you please enter Firmware Version: ")
 _WAN_1 = input("Could you please Enter speed and duplex, 100 Full or 1000 Full: ")
 os.system('cls')
 Logo_printer()
 print ( "\n\nSite Verification Start at: %s %s: %s cst" % (Test_date, Test_time_hour, Test_time_min))
 
 print("""\nSite Verification Information:-
-------------------------
  \n """ )
  
 print ("1. Bundle ID: %s" % MB)                #The sequence number need to be checked..!
 print ("2. PON Number:: %s" % PON)
 print ("3. POP : %s" % POP)
 print ("4. Site Address: %s" % Site)
 #print ("5. WAN Gateway #: %s" % Port)
 print ("6. Carrier Name: %s" % Carrier)
 print ("7. Circuit ID: %s" % CKT_ID)
 print ("8. MTE Public IP Address: %s" %MTEPublic)
 print ("9. Gateway IP %s" % GW)
 
 print ("Test Section:- \n")
 print ("--------------------------------------------------------------------------\n")
 print ("Serial Number: %s" %Serial)
 print ("Firmware Version: %s" %_Firm_Version)
 print ("WAN 1: %s" %_WAN_1)
 print ("""\nuse this command:  ping %s -c 5\n\n""" % MTEPublic) #Need to remove the \subnet
 print ("--------------------------------------------------------------------------\n")
 




