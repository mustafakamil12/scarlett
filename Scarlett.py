#My Template generator...!
import os
from copy import deepcopy
from Plant_Test_decision import Planet_Test_desc
from Site_verification_decision import Site_Verification_desc
from Network_Configuration_decision import Network_Configuration_desc
from Site_Activiation_decision import Site_Activition_desc
#from Download_Youtube_Vedios import Download_Vedios
import lib

#os.system('cls') # To Clear screen

print("""
 ____   ____    _    ____  _     _____ _____ _____
/ ___| / ___|  / \  |  _ \| |   | ____|_   _|_   _|
\___ \| |     / _ \ | |_) | |   |  _|   | |   | |
 ___) | |___ / ___ \|  _ <| |___| |___  | |   | |
|____/ \____/_/   \_\_| \_\_____|_____| |_|   |_| 2.5
""")

print ("""\nPlease select from the list below:-
=================================\n
1. Plant Test
2. Site Verification
3. Network Configuration
4. Site Activation
5. Vital Devices Configuration

\n """)

x = input("Enter your Choice please ...: ")  # <------
Main_Choice = int(x)



#********************************************************************
while True:


     if Main_Choice == 1:

       Planet_Test_desc()
       break

     elif Main_Choice == 2:

        Site_Verification_desc()
        break

     elif Main_Choice == 3:

        Network_Configuration_desc()
        break

     elif Main_Choice == 4:

        Site_Activition_desc()
        break

     elif Main_Choice == 5:


        break

     elif Main_Choice == 6:

        Download_Vedios ()
        break

     elif Main_Choice > 6 or Main_Choice < 1 :
        print ("Please Select a vaild Choice between 1 and 4")
        break
