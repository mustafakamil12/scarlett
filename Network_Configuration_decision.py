#Network Configuration Decision ...



import lib
from copy import deepcopy


def Network_Configuration_desc():

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
    TCIF_INFO = deepcopy(lib.TCIF_Rider_Eth(usr, passw, MB_NO))	
    lib.NETWORK_Config_T1(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], SerialNO, TCIF_INFO['PE'], TCIF_INFO['CPE'], TCIF_INFO['AS'])
    break
	 

  if  "Ethernet" in My_CKT_Type:
   ADVA_Type = lib.select_ADVA()
   if ADVA_Type == 1:
    SerialNO = input("Please Enter ADVA 825 Serial No.: ")
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider(usr, passw, Pon_Path))
    TCIF_INFO = deepcopy(lib.TCIF_Rider_Eth(usr, passw, MB_NO))	
    lib.NETWORK_Config_825(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], SerialNO, TCIF_INFO['PE'], TCIF_INFO['CPE'], TCIF_INFO['AS'], PON_INFO['STAG'])
    break
	
   if ADVA_Type == 2:
    SerialNO = input("Please Enter ADVA 114 Serial No.: ")
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider(usr, passw, Pon_Path))
    TCIF_INFO = deepcopy(lib.TCIF_Rider_Eth(usr, passw, MB_NO))	
    lib.NETWORK_Config_114(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], SerialNO, TCIF_INFO['PE'], TCIF_INFO['CPE'], TCIF_INFO['AS'], PON_INFO['STAG'])
    break
	
    
	 
  elif "Broadband" or "DIA" in My_CKT_Type:
    SerialNO = input("Please Enter Fortigate 60D Serial No.: ")
    #MB_INFO = deepcopy(lib.MB_Rider(usr, passw, MB_NO))
    Pon_Path = MB_INFO['pon_url']
    PON_INFO = deepcopy(lib.PON_Rider_Broad(usr, passw, Pon_Path))
    TCIF_INFO = deepcopy(lib.TCIF_Rider_Broadband(usr, passw, MB_NO))		
    lib.NETWORK_Config_Broadband(MB_INFO['MB'], MB_INFO['PON'], PON_INFO['ESR'], MB_INFO['Site'], PON_INFO['Port'], MB_INFO['Carrier'],  MB_INFO['CKT'], MB_INFO['POPID'], SerialNO, TCIF_INFO['MTE_Public'], TCIF_INFO['MTE_Gateway'], TCIF_INFO['Upload_BW'], TCIF_INFO['Lan_IP'], TCIF_INFO[' ESR_VTI_IP'], TCIF_INFO['MTE_VTI_IP'], TCIF_INFO['AS'])
    break
	
	
  else :
    print ("Couldn't Recognize what kind of Circuit is this....!")
    break
		 
		 
 return