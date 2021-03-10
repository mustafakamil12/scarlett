#This Mistro will work only on Vital Configuration

import os
from lib.Scarlett_Logo import *
import Vital



os.system('cls')
Logo_printer()


print("""\nPlease Select from the List Below:-
---------------------------\n
1. Single_891_Router
2. Single Router
3. Dual Router
""")

_selection = int(input("Enter Your Choice...: "))


def Vital_Selection():
	while True: 

		if _selection == 1 :
			Vital.Single_891_R()
			break
	
	
	
		elif _selection == 2 :

			print("""
	1. Single_New-R1
	2. Single_Switch_Change
	3. Single_Switch_New_Configuration_48PS
	4. Single_Switch_New_Configuration_24PS
    """)
			_Single_selection = int(input("Please select One from The List above...: "))

			if _Single_selection == 1:	
				Vital.Single_New-R1()
				break
			elif _Single_selection == 2:
				Vital.Single_Switch_Change()
				break
			elif _Single_selection == 3:
				Vital.Single_Switch_New_Configuration_48PS()
				break
			elif _Single_selection == 4:
				Vital.Single_Switch_New_Configuration_24PS()
				break
			break

		
		elif _selection == 3 :
	
			print("""
	1. DUAL_Existing_R1
	2. DUAL_Existing_R2
	3. DUAL_New_R1
	4. DUAL_New_R2
	5. DUAL_Switch_Change
	6. DUAL_Switch_New_Configuration_24PS
	7. DUAL_Switch_New_Configuration_48PS
	8. R01_Existing_Masergy
	9. R02_Existing_Masergy
	""")
			_Dual_selection = int (input("Plese Select One from The List above...: "))
	
	
			if _Dual_selection == 1:
				Vital.DUAL_Existing_R1()
				break
			elif _Dual_selection == 2:
				Vital.DUAL_Existing_R2()
				break
			elif _Dual_selection == 3:
				Vital.DUAL_New_R1()
				break
			elif _Dual_selection == 4:
				Vital.DUAL_New_R2()
				break
			elif _Dual_selection == 5:	
				Vital.DUAL_Switch_Change()
				break
			elif _Dual_selection == 6:
				Vital.DUAL_Switch_New_Configuration_24PS()
				break
			elif _Dual_selection == 7:
				Vital.DUAL_Switch_New_Configuration_48PS()
				break
			elif _Dual_selection == 8:
				Vital.R01_Existing_Masergy()
				break
			elif _Dual_selection == 9:
				Vital.R02_Existing_Masergy()
				break
		break

Vital_Selection()