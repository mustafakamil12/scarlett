# Steps had been made:-

def Config_tdm_Port_Sec (PON_No):
 #
  print (""" clock-source node-timed
                channel-group 1
                    description "PON %s"
                    encap-type bcp-dot1q
                    timeslots 1-24
                    no shutdown
                exit
                no shutdown""" % PON_No)		
  return				