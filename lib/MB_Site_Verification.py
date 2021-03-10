#Additional Information required for the Site Verification


def MB_add_SiteV_Info ():
 print ("""\nCould you please provide me with additionl information Required to help you more:- 
 Hint:- The information below are available in the JIRA...
===================================================\n""")

 _DMARC = input("DMARC information: ")
 _Device_Serial_No = input("Device Serial No.: ")
 _Tracking_No = input("Tracking No. if available:")

 return {'_DMARC': _DMARC, '_Device_Serial_No': _Device_Serial_No, '_Tracking_No': _Tracking_No}

