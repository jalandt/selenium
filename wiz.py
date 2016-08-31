#! /usr/bin/python
#Practicing script to go through wizard UPDATE NAME WHEN DONE WITH SCENARIO
#Firefox

#Setting to Firefox browser & setup
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()

#Launching browser and Connecting to IPADDRESS(source cred and change IP for variable)
print "Changing password to grack12, setting up smtp server (need real email and password), 2 users, each own workspace, all protocols enabled."
driver.get('http://192.168.1.148')
driver.implicitly_wait(10)

#Logging in with default information (simulates pressing Enter, not clicking the button)

login = driver.find_element_by_id("username-inputEl")
login.clear()
login.send_keys("admin")
password = driver.find_element_by_id("password-inputEl")
password.clear()
password.send_keys("gtech")
password.send_keys(Keys.RETURN)

#Selecting Agree on ToS
agree = driver.find_element_by_id("button-1027")
agree.click()

#Selecting M&E option for wizard
MnE = driver.find_element_by_id("button-1029")
MnE.click()

#Entering new password, confirming password, entering password questions and answers
newpass = driver.find_element_by_id("passwordfield-1034-inputEl")
newpass.send_keys("grack12")

cnfrmPwd = driver.find_element_by_id("passwordfield-1035-inputEl")
cnfrmPwd.send_keys("grack12")

q1 = driver.find_element_by_id("question1-inputEl")
q1.send_keys("question1")

a1 = driver.find_element_by_id("textfield-1036-inputEl")
a1.send_keys("answer1")

q2 = driver.find_element_by_id("textfield-1037-inputEl")
q2.send_keys("question2")

a2 = driver.find_element_by_id("textfield-1038-inputEl")
a2.send_keys("answer2")

q3 = driver.find_element_by_id("textfield-1039-inputEl")
q3.send_keys("question3")

a3 = driver.find_element_by_id("textfield-1040-inputEl")
a3.send_keys("answer3")

contPwd = driver.find_element_by_id("button-1044")
contPwd.click()

#Setting up SMTP server
emailtoggle = driver.find_element_by_id("checkbox-1046-inputEl")
emailtoggle.click()

smtpsrvr = driver.find_element_by_id("textfield-1048-inputEl")
smtpsrvr.send_keys("smtp.gmail.com")

ssltoggle = driver.find_element_by_id("checkbox-1050-inputEl")
ssltoggle.click()

sndr = driver.find_element_by_id("textfield-1051-inputEl")
sndr.send_keys("jdalandt@gmail.com")

authtoggle = driver.find_element_by_id("checkbox-1052-inputEl")
authtoggle.click()

usrname = driver.find_element_by_id("textfield-1053-inputEl")
usrname.send_keys("jdalandt@gmail.com")

#MAKE SURE TO ADD CORRECT PASSWORD AND E-MAIL ASK STEVE ROBERTS FOR CREATED ACCOUNT
emlpass = driver.find_element_by_id("passwordfield-1054-inputEl")
emlpass.send_keys("yeah-right")

sndTo = driver.find_element_by_id("textfield-1055-inputEl")
sndTo.send_keys("jdalandt@gmail.com")

emailcont = driver.find_element_by_id("button-1060")
emailcont.click()

#ADDING 2 USERS

adduser = driver.find_element_by_id("button-1066")
adduser.click()
driver.implicitly_wait(10)
#u1 = driver.find_element_by_id("textfield-1130-inputEl")
#u1.send_keys("james")
u1 = driver.find_element_by_css_selector("input[name='username']")
u1.click()
u1.send_keys("james")

p1 = driver.find_element_by_id("passwordfield-1131-inputEl")
p1.send_keys("grack12")
p1.send_keys(Keys.RETURN)

adduser.click()

u1.send_keys("steve")
p1.send_keys("grack12")
p1.send_keys(Keys.RETURN)

#Create workspace for each user (radiofield-1069) or one workspace (radiofield-1068)
#By default we create a workspace for each user. Change the value from 1069 to 1068 if you want just one workspace

ws = driver.find_element_by_id("radiofield-1069-inputEl")
ws.click()

usercont = driver.find_element_by_id("button-1074")
usercont.click()

#Selecting iSCSI (1076), Project shares(1077), Both(1078)
#Project shares only by default

fs = driver.find_element_by_id("radiofield-1077-inputEl")
fs.click()

type = driver.find_element_by_id("button-1082")
type.click()

#Protocol setup 
##ASK JAMES R HOW TO DO THIS, IT DOESN'T SEEM CLEAR WHAT TO CHOOSE. I DON'T SEE INPUTEL anywhere

pcallcont= driver.find_element_by_id("button-1099")
pcallcont.click()

#Confirm and create shares

cnfrm = driver.find_element_by_id("button-1113")
cnfrm.click()

create = driver.find_element_by_id("button-1014")
create.click()

driver.implicitly_wait(1200)
#log out
menu = driver.find_element_by_id("splitbutton-1022-btnEl")
menu.click()

logout = driver.find_element_by_id("menuitem-1027-itemEl")
logout.click()

locnfrm = driver.find_element_by_id("button-1006")
locnfrm.click()
