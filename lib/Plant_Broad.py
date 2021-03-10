# -- Planet Test --
import os
from datetime import datetime
#from lib.MB_Parent import *
from lib.Scarlett_Logo import *

def Planet_Test_Broad (MB, PON, POP, Site, Carrier,  CKT_ID, GW):
 dt = datetime.now()
 Test_date =  '{:%B %d %Y}'.format(dt)
 Test_time_hour = '{:%I }'.format(dt)
 Test_time_min = '{:%M %p}'.format(dt)
 os.system('cls')
 Logo_printer()
 print ( "\n\nTest Start at: %s %s: %s cst" % (Test_date, Test_time_hour, Test_time_min))
 
 print("""\nPlant Test Information:-
-------------------------
  \n """ )
  
 print ("1. Bundle ID: %s" % MB)                #The sequence number need to be checked..!
 print ("2. PON Number:: %s" % PON)
 print ("3. POP : %s" % POP)
 print ("4. Site Address: %s" % Site)
 print ("5. Carrier Name: %s" % Carrier)
 print ("6. Circuit ID: %s" % CKT_ID)
 print ("7. Gateway IP %s" % GW)
 
 print ("Test Section:- \n")
 print ("""\nuse this command:  ping %s -c 5 \n""" % GW)
 print ("--------------------------------------------------------------------------\n")
 




