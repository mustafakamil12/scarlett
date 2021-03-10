# -- Planet Test --

import os
from datetime import datetime
from lib.MB_Parent import *
from lib.Scarlett_Logo import *

def Planet_Test_Eth (MB, PON, ESR, Site, Port, Carrier,  CKT_ID, STAG):
 dt = datetime.now()
 Test_date =  '{:%B %d %Y}'.format(dt)
 Test_time_hour = '{:%I }'.format(dt)
 Test_time_min = '{:%M %p}'.format(dt)
 os.system('cls')
 Logo_printer()
 print ( "\n\nTest Start at: %s %s: %s cst" % (Test_date, Test_time_hour, Test_time_min))
 
 print("""\nPlanet Test Information:-
-------------------------
  \n """ )
  
 print ("1. Bundle ID: %s" % MB)                #The sequence number need to be checked..!
 print ("2. PON Number: %s" % PON)
 print ("3. ESR : %s" % ESR)
 print ("4. Site Address: %s" % Site)
 print ("5. Port No.: %s.%s" %(Port,STAG))
 print ("6. Carrier Name: %s" % Carrier)
 print ("7. Circuit ID: %s" % CKT_ID)
 print ("8. Need to check %s if it's up or down \n" % Port)
 
 print ("Test Section:- \n")
 print ("""\nuse this command:  show port %s \n""" % Port)
 print ("--------------------------------------------------------------------------\n")
 




