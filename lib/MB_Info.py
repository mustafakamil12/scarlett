# Here the main information will be uploaded

def MB_Main_Info ():
 print ("""\nCould you please provide me with information below:- 
===================================================\n""")
 _MB =  input("Bundle ID: ")
 _PON = input("PON Number: ")
 _ESR = input("ESR: ")
 _Site = input("Site Address: ")
 _Port = input("Port #: ")
 _Carrier = input("Carrier Name: ")
 _CKT_ID = input("Circuit ID: ")
 _GW_BB = input("If this is Broadband or DAI, please enter the Gateway IP: ")

 return {'MB' :_MB,  'PON' :_PON,  'ESR' :_ESR,  'Site' :_Site,  'Port': _Port,  'Carrier' :_Carrier,  'CKT_ID' :_CKT_ID, 'GW' : _GW_BB}