#Read the Port and find out it's dot1q or q in q

import sys

def Port_Rcog(Port, STAG):

 #_no_char = len (Port)
 
 if STAG != 0 :
   
  #PortMyList = list(Port)
  #PortMyList[5] = ':'
  #PortList = str(PortMyList)
  #PortList = "".join(PortMyList)
  PortList = Port+":"+STAG
  PortList += '.93'
  return (PortList)
 else:
  Port += ':93'
  return (Port)