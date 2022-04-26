#imports
from ctypes.util import find_library
from imp import PY_SOURCE
from tempfile import tempdir
from typing import final
import PyPDF2
from msedge.selenium_tools import Edge, EdgeOptions
from lib2to3.pgen2.driver import Driver
import time
import os
from telnetlib import SE
from time import sleep
from tkinter import Button
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import xlsxwriter

#Acessing microsoft edge
options = EdgeOptions()
options.use_chromium = True
options.add_argument("-inprivate")
options.binary_location = r"C:/Program Files (x86)/Microsoft/Edge\Application/msedge.exe"
driver = Edge(executable_path = r"C:/Users/ydves/Downloads/edgedriver_win64 (1)/msedgedriver.exe", options = options) # Modify the path here...



# #vitsting the website 
driver.get('https://www.ebi.ac.uk/ebisearch/search.ebi?db=chembl-document&query=antigen&size=15')
# #Going till save 
# time.sleep(1.8)
# pyautogui.click(955,881)
# time.sleep(0.8)
# pyautogui.click(1220,28)
# time.sleep(0.8)
# value=1
# for i in range(5):
#         if(i!=0):
#                 value+=1
#                 #to scroll through pages.
#                 driver.get('https://www.ebi.ac.uk/ebisearch/search.ebi?db=chembl-document&query=antigen&size=15&page='+str(value))
#                 time.sleep(0.8)
#                 pyautogui.click(1220,28)
#                 time.sleep(0.8)
#         try:
#                 pyautogui.click(540,829)
#                 time.sleep(0.8)
#                 pyautogui.click(585,736)
#                 time.sleep(0.8)

#                 #Selecting the format type.
#                 pyautogui.click(961,596)
#                 time.sleep(0.8)
#                 pyautogui.click(870,697)
#                 time.sleep(0.8)

#                 # #selecting the various types of data required
#                 pyautogui.click(982,633)
#                 time.sleep(0.8)

#                 #selecting data
#                 pyautogui.click(635,599)
#                 time.sleep(0.8)
#                 pyautogui.click(976,666)
#                 time.sleep(0.8)
#                 pyautogui.click(640,686)
#                 time.sleep(0.8)
#                 pyautogui.click(1003,596)
#                 time.sleep(0.8)
#                 #Scrolling
#                 for i in range (6):
#                         pyautogui.click(1293,849)
#                         time.sleep(0.1)
#                 pyautogui.sleep(0.5)
#                 pyautogui.click(1192,851)
#                 time.sleep(0.8)

                
#                 driver.quit
       
        
#         except KeyboardInterrupt:
#                 break

# #For chembl assay
# #for i in range(132):
#         if(i!=0):
#                 value+=1
#                 driver.get('https://www.ebi.ac.uk/ebisearch/search.ebi?db=chembl-assay&query=antigen&size=15&page='+str(value))
#                 time.sleep(0.8)
#                 pyautogui.click(1220,28)
#                 time.sleep(0.8)
#         try:
#                 pyautogui.click(540,829)
#                 time.sleep(0.8)
#                 pyautogui.click(585,736)
#                 time.sleep(0.8)

#                 #Selecting the format type.
#                 pyautogui.click(961,596)
#                 time.sleep(0.8)
#                 pyautogui.click(870,697)
#                 time.sleep(0.8)

#                 # #selecting the various types of data required
#                 pyautogui.click(982,633)
#                 time.sleep(0.8)
#                 #selecting data
#                 pyautogui.click(635,599)
#                 time.sleep(0.8)
#                 pyautogui.click(976,666)
#                 time.sleep(0.8)
#                 pyautogui.click(640,686)
#                 time.sleep(0.8)
#                 pyautogui.click(1003,596)
#                 time.sleep(0.8)
#                 #Scrolling
#                 for i in range (6):
#                         pyautogui.click(1293,849)
#                         time.sleep(0.1)
#                 pyautogui.sleep(0.5)
#                 pyautogui.click(1192,851)
#                 time.sleep(0.8)

                
#                 driver.quit
       
#         #to stop the code using keyborad interrupt.
#         except KeyboardInterrupt:
#                 break
