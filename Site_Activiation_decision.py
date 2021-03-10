#Site verification scene...!

import lib
from copy import deepcopy


def Site_Activition_desc():

 while True:

  

  #a = input("Enter your Choice please ...: ")
  #My_CKT_Type = int(a)

  My_Auth = deepcopy(lib.Get_Auth())
  usr = My_Auth['user']
  passw =   My_Auth['passwd']
  MB_NO =   My_Auth['MB_No']
  MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
  CKTType = MB_INFO['CKT_Type']

  if  "T1" in CKTType:
    SerialNO = input("Please Enter Overture Serial No.: ")
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider(usr, passw, Pon_Path))
    lib.Site_Activation_T1(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['MBCODE'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], SerialNO, MB_INFO['Bundle_Notes'])
    break

  elif "Ethernet" in CKTType:
    SerialNO = input("Please Enter ADVA Serial No.: ")
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider(usr, passw, Pon_Path))
    lib.Site_Activation_Eth(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['MBCODE'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], SerialNO, MB_INFO['Bundle_Notes'], PON_INFO['STAG'])
    break

  elif "Broadband" or "DIA" in CKTType:
    SerialNO = input("Please Enter Fortigate Serial No.: ")
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider(usr, passw, Pon_Path))
    lib.Site_Activation_Broad(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['MBCODE'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], SerialNO, MB_INFO['Bundle_Notes'], MB_INFO['POPID'])
    break


  else :
    print ("Couldn't Recognize what kind of Circuit is this....!")
    break


 return
