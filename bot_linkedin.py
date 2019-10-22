from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
from time import sleep, strftime
import sys

def login():

    user = input("Email:")
    username = driver.find_element_by_name('session_key')
    username.send_keys(user)
    
    password_input = input("Password:")
    password = driver.find_element_by_name('session_password')
    
    password.send_keys(password_input)
    button_login = driver.find_element_by_css_selector('#app__container > main > div > form > div.login__form_action_container > button')
    button_login.click()
    sleep(3)
    print("success")
def goto_network():
 try:
   driver.find_element_by_id("mynetwork-tab-icon").click()
 except:
   print("[+] Some Error Occoured \n Directly opening networks tab")
   body = driver.find_element_by_tag_name("body")
   body.send_keys(Keys.CONTROL + 't')
   driver.get(nurl)
def get_details():
 #test = input(" start sending requests (y/n)")
 #b = input("Numarul de conectari:")
 #search=driver.find_element_by_xpath('//*[@id="ember34"]/input')
 #search.send_keys("recruiters")
 #btn_search=driver.find_element_by_css_selector('#ember32 > div.search-global-typeahead__controls > button')
 #btn_search.click()
 b = int(sys.argv[1])
 #b = int(b)  # parse string into an integer
 for i in range(0,b):
   #button_inv = driver.find_element_by_xpath('//*[@id="ember25"]/div[2]')
   #button_inv.click()
   driver.get(nurl)
   sleep(5)
   pag.click(800,740)
   #pag.click(1150,315)
   sleep(3)
   print("["+str(i)+"] Connection request sent ")
   print("done")   

driver = webdriver.Chrome('C:/Users/andre/Desktop/train&personal/chromedriver.exe')
url = "https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin"
nurl = "http://linkedin.com/mynetwork/"
driver = webdriver.Chrome('C:/Users/andre/Desktop/train&personal/chromedriver.exe')
driver.get(url)

login()
goto_network()
get_details()
