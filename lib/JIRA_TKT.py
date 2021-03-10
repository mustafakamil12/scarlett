#This Code is to open Jira tkt and return back Jira tkt to the system...

import os
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import *
from time import sleep
from copy import deepcopy

def Jira_tkt_Creator():
 Jira_url = "https://jira.masergy.com/secure/Dashboard.jspa"
 user = "malogaidi"
 password = "P@ss1979"
 driver = webdriver.Firefox()
 driver.get(Jira_url)
 sleep(5)
 
 elem = driver.find_element_by_id("login-form-username")
 elem.send_keys(user)
 elem = driver.find_element_by_id("login-form-password")
 elem.send_keys(password)
 elem.send_keys(Keys.RETURN)
 sleep(3)
 driver.find_element_by_id("create_link").click()
 sleep(3)
 Issue_Type = driver.find_element_by_id("issuetype-field")
 Issue_Type.clear()
 Issue_Type.send_keys("Prep") 
 
 #selection.select_by_visible_text("Prep")
 
 
 #driver.close()
 
Jira_tkt_Creator()  