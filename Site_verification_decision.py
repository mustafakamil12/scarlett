#Site verification scene...!

import lib
from copy import deepcopy


def Site_Verification_desc():

 while True:

  

  #a = input("Enter your Choice please ...: ")
  #My_CKT_Type = int(a)

  My_Auth = deepcopy(lib.Get_Auth())
  usr = My_Auth['user']
  passw =   My_Auth['passwd']
  MB_NO =   My_Auth['MB_No']
  MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
  My_CKT_Type = MB_INFO['CKT_Type']

  if  "T1" in My_CKT_Type:
    SerialNO = input("Please Enter Overture Serial No.: ")
    
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider(usr, passw, Pon_Path))
    lib.Verification_Test_T1(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], SerialNO, MB_INFO['POPID'])
    break

  if  "Ethernet" in My_CKT_Type:
   ADVA_Type = lib.select_ADVA()  
  
   if ADVA_Type == 1:
    SerialNO = input("Please Enter ADVA Serial No.: ")
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider(usr, passw, Pon_Path))
    lib.Verification_Test_825(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], SerialNO, PON_INFO['STAG'])
    break

   elif ADVA_Type == 2:
    SerialNO = input("Please Enter ADVA Serial No.: ")
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider(usr, passw, Pon_Path))
    lib.Verification_Test_114(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], SerialNO, PON_INFO['STAG'])
    break
	

  elif "Broadband" or "DIA" in My_CKT_Type:
    SerialNO = input("Please Enter Fortigate 60D Serial No.: ")
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider_Broad(usr, passw, Pon_Path))
    TCIF_INFO = deepcopy(lib.TCIF_Rider_Broadband(usr, passw, MB_NO))
    lib.Site_Verification_Broad (MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['Site'], TCIF_INFO['MTE_Gateway'], MB_INFO['Carrier'],  MB_INFO['CKT'], SerialNO,   MB_INFO['POPID'], TCIF_INFO['MTE_Public'])
    break


  else :
    print ("Couldn't Recognize what kind of Circuit is this....!")
    break


 return