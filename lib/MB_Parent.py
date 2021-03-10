# This is MB_Parent Module 
# We will use this Module as parent for all other Modules...!


class MB_Parent:
   'This is the Parent Class for all the project'
        		 
   def __init__ (self, MB, PON, ESR, Site, Port, Carrier,  CKT_ID, GW):
        #
        self.MB = MB
        self.PON = PON  
        self.ESR = ESR 
        self.Site = Site
        self.Port = Port 
        self.Carrier = Carrier
        self.CKT_ID = CKT_ID
        self.GW = GW
 
   def Parent_Info(self):
        #  
	     print ("%s  Information:-" % self.MB, self.MB, self.PON, self.ESR , self.Site, self.Port, self.Carrier, self.CKT_ID)