#Site Activiation for T1...

import os
from datetime import datetime
from lib.MB_Parent import *
from lib.Activation_T1_Checklist import *
from lib.Scarlett_Logo import *

def Site_Activation_T1 (MB, PON, ESR, SiteID, Site, Port, Carrier, CKT_ID, Serial, Bundle_Notes):
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

 _S_OR_D_CKT = input("1. single or dual Circuit: ") # Can we check this using the landscape or throgh any other way??
 
 print ("2. Type of Service: T1")
 print ("3. Site Address: %s" % Site)
 print ("4. Bundle ID: %s" % MB)
 print ("5. Site ID: %s" %SiteID)
 print ("6. PON Number: %s" % PON)
 print ("7. ESR: %s" %ESR)
 print ("8. Port: %s" %Port)
 print ("9. Carrier Name: %s" % Carrier)
 print ("10. Circuit ID: %s" % CKT_ID)

 _Activ_tkt = input("Creat Jira TKT for Activation - ")
 print("11. Activation TKT: %s" %_Activ_tkt)

 print("12. Bundle information:\n")
 print(Bundle_Notes)
 print("\nWhat Need to verify in this Circuit\n")

 Activation_T1_check()

 print("\n13. prepare the Begining Activation email.")

 print("\n\n14. Follow up the Activation Excell Tamplete.")

 print("\n15. Send the actviation complete email.")

 print("\n16. add the tamplete to the share drive and change the name to ")
