from ctypes.util import find_library
from inspect import ArgInfo 
from operator import le
from typing import final
import PyPDF2
from msedge.selenium_tools import Edge, EdgeOptions
from email import message
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
#BCM
account=[("eshan.yadav2020@vitstudent.ac.in","JvnP530#"),("meenakshi.rajesh2020@vitstudent.ac.in","PkqZ322%"),("aparna.vivek2020@vitstudent.ac.in","RfrT929&"),("rajendran.p2020@vitstudent.ac.in","BzdS173%"),("sharmishta.ganesh2020@vitstudent.ac.in","babyGanesh4983."),("subhradyuti.basu2020@vitstudent.ac.in","UpbeatPanda@99"),("akhil.ajin2020@vitstudent.ac.in","ZxoS926$"),("harshini.a2020@vitstudent.ac.in","Harshu@2003"),("sakshiraghavan.a2020@vitstudent.ac.in","#YougotitEshan")]
print(len(account))
branches=[('BCL', 'BCB'), ('BEE', 'BCM'), ('BBT', 'BCE'), ('BMA', 'BME'), ('BML', 'BCI'), ('BCT', 'BMM'), ('BBS', 'BEI'), ('BIT', 'BEC'), ('BDS', 'BKT')]
for TB_acc_count in range(len(account)):
    for reg in branches[TB_acc_count]:            
        file_count=1
        if  reg=="BBT":
            file_count+=1
            continue

        #opening the pdf.
        pdf=open('EPT Schedule _ Fresher 2021 - All B. tech programs.pdf','rb')
        file_obj=PyPDF2.PdfFileReader(pdf)
        #information of one page.
        all_info=[]
        final=[] 
        for i in range(file_obj.numPages):
            #extrating information
            all_info=file_obj.getPage(i).extractText().split("\n")
            if(i==0):
                count=10
            else:
                count=1
            
            while(count<len(all_info)):
                temp=str(all_info[count])
                if(temp.find(reg)!=-1):
                    final.append(all_info[count+1]+" "+all_info[count])  
                count+=7

        #final list of reg numbers
        reg_numbers=[]
        for i in range(len(final)):
            reg_numbers.append(final[i])
        print("These are the reg Numbers you are working with:-")
        print(reg_numbers)
        
        #TODO:create files for everyone.
        file_name=account[TB_acc_count][0]+"_file"+str(file_count)+".xlsx"
        # with open(file_name, 'w') as fp:
        #     for i in reg_numbers:
        #         fp.write(i+"\n")
        workbook = xlsxwriter.Workbook(file_name)
        worksheet = workbook.add_worksheet()
        ex_count=1
        for i in reg_numbers:
            worksheet.write('A'+str(ex_count),i[-9:])
            worksheet.write('B'+str(ex_count),i[:len(i)])
            ex_count+=1
        workbook.close()
        
        #------------------------------------------------------------------------------------------------------------------
        #opening MS Teams
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument("-inprivate")
        options.binary_location = r"C:/Program Files (x86)/Microsoft/Edge\Application/msedge.exe"
        driver = Edge(executable_path = r"C:/sem 4/Web Scraping/msedgedriver.exe", options = options) # Modify the path here...

        # Logging in
        driver.get("https://teams.microsoft.com/_?culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school/conversations/General?threadId=19:45LfYEyF-sT7Xd4QxqeMu5JhJw-w24MEM9sdi6GqaUw1@thread.tacv2&ctx=channel")
        driver.implicitly_wait(20)

        #reg No
        user_name=driver.find_element_by_id("i0116")
        user_name.send_keys(account[TB_acc_count][0])
        button=driver.find_element_by_id("idSIButton9")
        button.click()

        #password
        driver.implicitly_wait(20)
        paswrd=driver.find_element_by_id("i0118")
        paswrd.send_keys(account[TB_acc_count][1])

        WebDriverWait(driver,30).until(
            EC.text_to_be_present_in_element(
                (By.XPATH,'//*[@id="loginHeader"]/div'),
                "Enter password"
            )
        )
        button=driver.find_element_by_xpath('//*[@id="idSIButton9"]')
        button.click()

        #stay signed in
        WebDriverWait(driver,30).until(
            EC.text_to_be_present_in_element(
                (By.XPATH,'//*[@id="lightbox"]/div[3]/div/div[2]/div/div[1]'),
                "Stay signed in?"
            )
        )
        button=driver.find_element_by_xpath('//*[@id="idSIButton9"]')
        button.click()


        WebDriverWait(driver,30).until(
            EC.text_to_be_present_in_element(
                (By.XPATH,'//*[@id="teams-grid-title"]'),
                "Teams"
            )
        )
            
        #TESTING:
        # reg_numbers=["20BBT0226","20BBT0099","20MSI0089"]
        print("Enter the reg Numbers:")
        reg_numbers=['ADIBA FAIYAZ 21BCT0132', 'UTHISH SHIVA KAARTHIK R 21BCT0231', 'GAUTAM NARAIN VATS 21BCT0329', 'SHREYANSH SOMANI 21BCT0336', 'MEDHAVI SAXENA 21BDS0050', 'C JEEVAN REDDY 21BDS0129', 'RITESH SINGH 21BDS0227', 'SAKSHAM JAIN 21BDS0239', 'HARSH AGRAWAL 21BDS0272', 'TANMAY AGARWAL 21BDS0347', 'TANISH CHAUHAN 21BEC0043', 'ASMIT GHOSH 21BEC0049', 'SNEHA GUPTA 21BEC0360', 'ADITYA SHARMA 21BEC0648', 'SALONI PATTANAYAK 21BEC0916', 'DIVYANSH SHRIVASTAVA 21BEC0926', 'PUNARV SHARMA 21BEC0995', 'MANAN MATHUR 21BEC2002', 'PRIYANSHI JAIN 21BEE0002', 'GOKULL SRIDHAR 21BEE0017', 'ASHHAD MALIK 21BEE0044', 'PANKHURI KAPOOR 21BEE0083', 'GARVIT ARORA 21BEE0099', 'SHREEMAY KUMAR BHUYAN 21BEE0100', 'UMAIR MAJIEED 21BEE0124', 'DIVYA A JAGWANI 21BEE0126', 'SAKSHI AGRAWAL 21BEE0184', 'SIDHARTH KUMAR 21BEE0221', 'VANGARU ANANYA 21BEE0236', 'DILSHAD KHAN 21BEE0275']
        # Sending the message.
        for i in range(len(reg_numbers)):
            time.sleep(1)
            Search_Bar=driver.find_element_by_name("search-input-field")
            time.sleep(1)
            ActionChains(driver).double_click(Search_Bar).perform()
            # time.sleep(1)
            # Search_Bar.send_keys(Keys.CONTROL+"A")
            # time.sleep(1)
            # Search_Bar.send_keys(Keys.BACK_SPACE)
            # time.sleep(1)
            Search_Bar.clear()
            Search_Bar.send_keys(reg_numbers[i])
            time.sleep(1)
            Search_Bar.send_keys(u'\ue007')

            # WebDriverWait(driver,30).until(
            #     EC.text_to_be_present_in_element(
            #         (By.XPATH,'//*[@id="search-result-tabs"]/li[1]/a/span'),
            #         "Message"
            #     )
            # )
            time.sleep(2)
            # people=driver.find_element_by_xpath("//*[@id=\"search-result-tabs\"]/li[2]/a")
            # people.click()
            pyautogui.click(x=400,y=276)
            
            
            
            # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"peopleSearchContent-0\"]/div"))).click()
            # # paticular_person=driver.find_element_by_xpath("//*[@id=\"peopleSearchContent-0\"]/div")
            # # paticular_person.click()
            # time.sleep(2)
            time.sleep(3)
            pyautogui.click(x=286,y=340)
            time.sleep(4)
            
                            
            # ActionChains(driver).send_keys("Greetings Dear Reader,").perform()
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')


            time.sleep(1.5)

            # ActionChains(driver).send_keys("You are currently reading a message received to you by a bot built in 4 days by a single person of our team. Cool rgt?").perform()
            #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press(['enter','enter']) 
            # ActionChains(driver).send_keys("If that does not intrigue you I have got something more to tell you,").perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            # ActionChains(driver).send_keys('We, at *Alpha Bio Cell*, train you not only in technical skills like Web Dev, App Dev, ML, creating projects in real life with our team of experts and colleagues, network with big Giant Tech companies like we _Had_ done in past with Cisco, learn to write cold mails, manage finances to organize some of the biggest events of VIT plus to finance projects on board, be an awesome event manager, enhance your team building and give you plenty of opportunities to hone your leadership skills but also work on one of the most needed art of this 21st century industry, whether it is the corporate world, start-up world, foreign academic front, *the* skill that will make you stand out among a crowd of people you will be competing with is: The Art of Selling aka "Pitching".').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            # ActionChains(driver).send_keys('You will be trained and required to employ the skill of pitching for every task with us, from working in Management domain to Research domain to Technical domain, whichever one you join, you will surely be a different person with much more skills you currently have after you join Alpha Bio Cell- _A bio-entrepreneurship club created with a vision to be a platform to gather all like-minded people dedicated towards genuine personal growth__ .').perform()
            
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            # ActionChains(driver).send_keys('You are warmly welcomed to be a part of club Alpha Bio Cell, to start *YOUR* journey of personal growth.').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            # ActionChains(driver).send_keys('Register for our recruitments NOW !').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press(['enter','enter'])
            # ActionChains(driver).send_keys('-> Register in VTOP for recruitments under "Recruitments : Alpha Bio Cell" *Compulsorily*.').perform()

            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            # ActionChains(driver).send_keys('-> Fill in the following Pre-recruitment form to help us know which domain _you_ are interested in.The form also contains a whatsapp link to our group so please do join.').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            # ActionChains(driver).send_keys('https://docs.google.com/forms/d/e/1FAIpQLSd0IALOIb07Q2wc-7hMsR8sggTCvKIf90IwWbo51uaWX02OVg/viewform').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press(['enter','enter'])
            # ActionChains(driver).send_keys('-> To witness the perfect balance of "learning combined with fun" in our Club check out our Instagram:').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            # ActionChains(driver).send_keys('https://www.instagram.com/alphabiocell/?igshid=qpop2jfdl6bp').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press(['enter','enter'])

            # ActionChains(driver).send_keys('Details about our Recruitments !').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            # ActionChains(driver).send_keys('Dates: 5th February 2022-7th February 2022').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            # ActionChains(driver).send_keys('Register and mark your calendar for these dates !').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            # ActionChains(driver).send_keys('Excited to see you Onboard and start new adventures !!').perform()
            # #  time.sleep(0.5)
            # with pyautogui.hold('shift'):
            #         pyautogui.press('enter')
            
            with pyautogui.hold('ctrl'):
                    pyautogui.press('v')
            time.sleep(1)
            ActionChains(driver).send_keys(u'\ue007').perform()
            time.sleep(2)
            
            # time.sleep(3)
            # ActionChains(driver).send_keys(u'\ue007').perform()
            # time.sleep(2)
    
        driver.close()
        file_count+=1

   
