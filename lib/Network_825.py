#Network Configuration for Ethernet ADVA-825


import os
from datetime import datetime
from lib.MB_Parent import *
from lib.Scarlett_Logo import *

def NETWORK_Config_825 (MB, PON, ESR, Site, Port, Carrier,  CKT_ID,  Serial, PE, CPE, AS, STAG):
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

 
10. Landscape and TCIF information:-\n""" %MB)
 
 print("ESR and Port Inof:\n")
 Port=Port+"."+STAG
 print(ESR, Port)
 
 print("""\nPE IP Address:	%s
CE IP Address:	%s
CE BGP ASN:	%s\n""" %(PE, CPE, AS))
 
 print("""\n11. CAS information:- \n""")
 print("\n\n12. Vlan: \n")
 
 print("13) Product Type: \n")



 print ("14) Circuit Type: ")


   

 print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

 
 print("15 ) Configuration:- \n\n")