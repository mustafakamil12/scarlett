#Site Activiation for Ethernet...

import os
from datetime import datetime
from lib.MB_Parent import *
from lib.Activation_Broad_Checklist import *
from lib.Scarlett_Logo import *

def Site_Activation_Broad (MB, PON, ESR, MBCODE,Site, Port, Carrier,  CKT_ID, Serial, BundleNotes, POPID):
 dt = datetime.now()
 Test_date =  '{:%B %d %Y}'.format(dt)
 Test_time_hour = '{:%I }'.format(dt)
 Test_time_min = '{:%M %p}'.format(dt)
 os.system('cls')
 Logo_printer()
 print ( "\n\nSite Activation Start at: %s %s: %s cst" % (Test_date, Test_time_hour, Test_time_min))
 
 print("""\nSite Activation Information:-
-------------------------
  \n """ )
 
 _S_OR_D_CKT = input("1. single or dual Circuit: ")
  
 print ("2. Type of Service: Broadband")
 print ("3. Site Address: %s" % Site)
 print ("4. Bundle ID: %s" % MB)  
 print ("5. Site ID: %s" %MBCODE)
 print ("6. PON Number: %s" % PON)
 print("7. POP: %s" %POPID)
 
 print ("8. Carrier Name: %s" % Carrier)
 print ("9. Circuit ID: %s" % CKT_ID)
 
 _Activ_tkt = input("Creat Jira TKT for Activation - ")
 print("10. Avtivation TKT: %s" %_Activ_tkt)
 
 print("11. Bundle information:\n")
 print(BundleNotes)
 print("\nWhat Need to verify in this Circuit\n")

 Activation_Broad_check()
 
 print("\n13. prepare the Begining Activation email.")

 print("\n14. Follow up the Activation Excell Tamplete.")

 print("\n15. Send the actviation complete email.")

 print("\n16. add the tamplete to the share drive and change the name to ")