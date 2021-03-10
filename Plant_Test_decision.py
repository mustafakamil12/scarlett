import lib
from copy import deepcopy



def Planet_Test_desc():

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
    
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider(usr, passw, Pon_Path))
    lib.Planet_Test_T1(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'])
    break
	 
  elif "Ethernet" in CKTType:
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider(usr, passw, Pon_Path))
    lib.Planet_Test_Eth(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], PON_INFO['STAG'])
    break
	
  elif "Broadband" or "DIA" in CKTType:
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    #PON_INFO = deepcopy(lib.PON_Rider_Broad(usr, passw, Pon_Path))
    TCIF_INFO = deepcopy(lib.TCIF_Rider_Broadband(usr, passw, MB_NO))
    lib.Planet_Test_Broad(MB_INFO['MB'], MB_INFO['PON'], MB_INFO['POPID'], MB_INFO['Site'],  MB_INFO['Carrier'],  MB_INFO['CKT'], TCIF_INFO['MTE_Gateway'])
    break
	
	
  else :
    print ("Couldn't Recognize what kind of Circuit is this....!")
    break
		 
		 
 return