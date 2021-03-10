# -- Planet Test --

import os
from datetime import datetime
from lib.MB_Parent import *
from lib.Scarlett_Logo import *


def Planet_Test_T1 (MB, PON, ESR, Site, Port, Carrier,  CKT_ID):
 os.system('cls')
 dt = datetime.now()
 Test_date =  '{:%B %d %Y}'.format(dt)
 Test_time_hour = '{:%I }'.format(dt)
 Test_time_min = '{:%M %p}'.format(dt)
 
 Logo_printer()
 
 print ( "\n\nTest Start at: %s %s: %s cst" % (Test_date, Test_time_hour, Test_time_min))
 
 print("""\nPlanet Test Information:-
-------------------------
  \n """ )
  
 print ("1. Bundle ID: %s" % MB)                #The sequence number need to be checked..!
 print ("2. PON Number: %s" % PON)
 print ("3. ESR : %s" % ESR)
 print ("4. Site Address: %s" % Site)
 print ("5. Port #: %s" % Port)
 print ("6. Carrier Name: %s" % Carrier)
 print ("7. Circuit ID: %s" % CKT_ID)
 print ("\n8. Configuration Section \n")
 print ("""   show port %s 
   configure port x/y/z tdm ds1 a.b.c
   info \n
 """ %Port)
 print ("""  clock-source node-timed
                channel-group 1
                    description "PON %s"
                    encap-type bcp-dot1q
                    timeslots 1-24
                    no shutdown
                exit
                no shutdown \n""" % PON)	
				
 print ("Test Section:- \n")
 print ("""\n2e23 Test for 45 minutes ... bert 2e23 duration 2700 \n""")
 print ("\n--------------------------------------------------------------------------")
 print ("""\nZeros Test for 5 minutes ... bert zeros duration 300 \n""")
 print ("\n--------------------------------------------------------------------------")
 print ("""\nOnes Test for 5 minutes ... bert ones duration 300 \n""")
 




