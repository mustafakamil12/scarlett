#Reading the main information from the landscape...!
import os
#import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import *
from time import sleep
from copy import deepcopy

def MB_Rider(userlog, passlog, MBNO):
    user = userlog
    password = passlog
    driver = webdriver.Firefox()
    url = "https://landscape.masergy.com/landscape/#/support/bundle/"+MBNO
    driver.get(url)
    sleep(5)

    elem = driver.find_element_by_id("username")
    elem.send_keys(user)
    elem = driver.find_element_by_id("password")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    sleep(2)

    try:
     Invalid_Testing = driver.find_element_by_xpath("//span[@class='kc-feedback-text']")
     if 'Invalid' in Invalid_Testing.text:
      print("\nInvalid username or password.")
      driver.close()
      quit()
    except NoSuchElementException:
     print("Start Process...!")

    sleep(12)
    MB = driver.find_element_by_class_name("col-md-9").text



    Site = driver.find_element_by_id("title").text

    MBCODE = Site[11:18]

    Carrier = driver.find_element_by_xpath("//tr[@ng-repeat='segment in $ctrl.bdleSegments | orderBy:orderByField:reverseSort | filter:$ctrl.segmentSearch track by $index']//td[4]").text
    CKT = driver.find_element_by_xpath("//tr[@ng-repeat='segment in $ctrl.bdleSegments | orderBy:orderByField:reverseSort | filter:$ctrl.segmentSearch track by $index']//td[5]").text
    #sleep(10)
    Bundle_Notes = driver.find_element_by_xpath("//textarea[@ng-model='msgyBdlNotesVM.bundleNotes']").get_attribute('value')
    CKT_Type = driver.find_element_by_xpath("//div[@class='panel-body']//form[@class='form-horizontal ng-pristine ng-valid']//div[@class='col-sm-2'][4]//div[@class='form-group'][3]//div[@class='col-sm-6']//p[@class='form-control-static']").text
    #print("CKT_Type: ", CKT_Type)
    POPID = driver.find_element_by_xpath("//form[@class='form-horizontal ng-pristine ng-valid']//div[@class='row']//div[@class='col-sm-2'][4]//div[5]//div[@class='col-sm-6']//p[@class='form-control-static']").text

    #=================================================

    try:
     PON1 = driver.find_element_by_xpath("//span[@ng-repeat][1]")
     PON1 = PON1.text
    except NoSuchElementException:
     PON1 = 0

    try:
     PON2 = driver.find_element_by_xpath("//span[@ng-repeat][2]")
     PON2 = PON2.text
    except NoSuchElementException:
     PON2 = 0

    try:
     PON3 = driver.find_element_by_xpath("//span[@ng-repeat][3]")
     PON3 = PON3.text
    except NoSuchElementException:
     PON3 = 0
    try:
     PON4 = driver.find_element_by_xpath("//span[@ng-repeat][4]")
     PON4 = PON4.text
    except NoSuchElementException:
     PON4 = 0


    if (PON1 != 0 and PON2 == 0 and PON3 == 0 and PON4 == 0):
     PON = PON1

    elif (PON1 !=0 and (PON2 !=0 or PON3 !=0 or PON4 !=0) ):
     print("\nPlease advise that this bundle have more than one PON")
     print("\nCould you please select which PON you need to work with: ")
     z = {}
     if PON1 != 0:
      z = {'PON1': PON1}
     if PON2 != 0:
      z['PON2'] = PON2
     if PON3 != 0:
      z ['PON3'] = PON3
     if PON4 != 0:
      z ['PON4'] = PON4
     for _i, _v in z.items():
      print(_i, _v)

     PON = input("Please Enter PON Number you need to work on: ")
     PON =''.join(PON.split())

    #=================================================
    pon_url = "https://landscape.masergy.com/landscape/#/serviceDelivery/circuitManager/"+PON
    driver.close()

    return{'MB':MB[0:8], 'MBCODE': MBCODE, 'PON':PON, 'Site':Site[21:], 'Carrier':Carrier, 'CKT':CKT, 'Bundle_Notes':Bundle_Notes, 'pon_url':pon_url, 'POPID':POPID, 'CKT_Type':CKT_Type}

def PON_Rider(userlog, passlog, PonURL):
    user = userlog
    password = passlog
    _pon_driver = webdriver.Firefox()
    _pon_driver.get(PonURL)

    sleep(6)
    elem_p = _pon_driver.find_element_by_id("username")
    elem_p.send_keys(user)
    elem_p = _pon_driver.find_element_by_id("password")
    elem_p.send_keys(password)
    elem_p.send_keys(Keys.RETURN)

    sleep(15)
    ESR = _pon_driver.find_element_by_xpath("//span[@ng-if='$ctrl.networkObject']//small[1]").text
    Port = _pon_driver.find_element_by_xpath("//span[@ng-if='$ctrl.networkObject']//small[2]").text
    try:
      STAG = _pon_driver.find_element_by_xpath("//span[@ng-if='$ctrl.networkObject']//small[3]").text
      #STAG = STAG.text
    except NoSuchElementException:
	     STAG = ""
    _pon_driver.close()
    return{ 'ESR':ESR, 'Port':Port, 'STAG':STAG}



def PON_Rider_Broad(userlog, passlog, PonURL):
    user = userlog
    password = passlog
    _pon_driver = webdriver.Firefox()
    _pon_driver.get(PonURL)

    sleep(6)
    elem_p = _pon_driver.find_element_by_id("username")
    elem_p.send_keys(user)
    elem_p = _pon_driver.find_element_by_id("password")
    elem_p.send_keys(password)
    elem_p.send_keys(Keys.RETURN)

    sleep(15)
    ESR = _pon_driver.find_element_by_xpath("//span[@ng-if='$ctrl.networkObject']//small[1]").text
    Port = _pon_driver.find_element_by_xpath("//span[@ng-if='$ctrl.networkObject']//small[2]").text
    _pon_driver.close()

    return{ 'ESR':ESR, 'Port':Port}


def TCIF_Rider_Eth(userlog, passlog, MBNO):
    user = userlog
    password = passlog
    TCIF_driver = webdriver.Firefox()
    TCIF_Path = "https://landscape.masergy.com/landscape/#/serviceDelivery/cif/tcif/"+MBNO
    TCIF_driver.get (TCIF_Path)

    sleep(6)
    elem_T = TCIF_driver.find_element_by_id("username")
    elem_T.send_keys(user)
    elem_T = TCIF_driver.find_element_by_id("password")
    elem_T.send_keys(password)
    elem_T.send_keys(Keys.RETURN)

    sleep(15)
    PE = TCIF_driver.find_element_by_xpath("//input[@id='Masergy PE Interface / Mask (CIDR Notation)']").get_attribute('value')
    CPE = TCIF_driver.find_element_by_xpath("//input[@id='CPE Interface']").get_attribute('value')
    AS = TCIF_driver.find_element_by_xpath("//input[@id='Customer AS Number']").get_attribute('value')
    TCIF_driver.close()
    return{ 'PE':PE, 'CPE':CPE, 'AS':AS}




def TCIF_Rider_Broadband(userlog, passlog, MBNO):
    user = userlog
    password = passlog

    TCIF_driver = webdriver.Firefox()
    TCIF_Path = "https://landscape.masergy.com/landscape/#/serviceDelivery/cif/tcif/"+MBNO
    TCIF_driver.get (TCIF_Path)
    sleep(6)

    elem_T = TCIF_driver.find_element_by_id("username")
    elem_T.send_keys(user)
    elem_T = TCIF_driver.find_element_by_id("password")
    elem_T.send_keys(password)
    elem_T.send_keys(Keys.RETURN)
    sleep(15)

    MTE_Public = TCIF_driver.find_element_by_xpath("//input[@id='Static Public WAN IP Address with Subnet Mask']").get_attribute('value')
    MTE_Gateway = TCIF_driver.find_element_by_xpath("//input[@id='WAN Gateway IP Address']").get_attribute('value')
    Upload_BW  = TCIF_driver.find_element_by_xpath("//input[@id='Site Internet Upload Bandwidth']").get_attribute('value')
    Lan_IP  = TCIF_driver.find_element_by_xpath("//input[@id='LAN Interface IP Address with Subnet Mask']").get_attribute('value')
    ESR_VTI_IP  = TCIF_driver.find_element_by_xpath("//input[@id='Alcatel Tunnel Interface IP with Subnet Mask']").get_attribute('value')
    MTE_VTI_IP = TCIF_driver.find_element_by_xpath("//input[@id='CPE Tunnel Interface BGP IP']").get_attribute('value')
    AS = TCIF_driver.find_element_by_xpath("//input[@id='Site AS Number']").get_attribute('value')
    TCIF_driver.close()
    return{ 'MTE_Public':MTE_Public, 'MTE_Gateway':MTE_Gateway, 'Upload_BW':Upload_BW, 'Lan_IP': Lan_IP, ' ESR_VTI_IP':  ESR_VTI_IP, 'MTE_VTI_IP':MTE_VTI_IP, 'AS':AS}






def Get_Auth():
 user = "malogaidi"
 passwd = "P@ss2012"
 MB_No = input("Give Me Your MB No. please...: ")
 MB_No = ''.join(MB_No.split())
 return{'user':user, 'passwd':passwd, 'MB_No':MB_No}

#LandScape_Rider()
