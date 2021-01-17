from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os,wget

########################################################################
# Set ChromeDriverPath or use the Script ChromeDriver.py    
# it will download the compatible chromedriver to your user home repo  
# Set FB User & Pass    
########################################################################



fbuser = "" 
fbpass = ""
chromeDriver = "c:/users/joe/chromedriver.exe"
site =  'https://tinder.com'

class browser:
    def __init__(self, driver,DEFAULT_TIMEOUT,delay):
        self.timeout = DEFAULT_TIMEOUT
        self.delay = delay
        self.driver = driver
        self.chrome_options = webdriver.ChromeOptions()

    def enable_download_headless(self,download_dir):
        self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        self.driver.execute("send_command", params)

    def element(self,xpath):
        self.Welement = WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def click(self):
            self.Welement.click()
            sleep(1)

    def send(self,text):
            self.Welement.send_keys(text)

    def get(self,site):
        self.driver.get(site)
        sleep(4)

    def Execute(self,scripts):
        self.driver.execute_script(scripts,self.Welement)

    def text(self):
        return self.Welement.text

    def attribute(self,att):
        return self.Welement.get_attribute(att)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=2')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-popup-blocking')
driver = webdriver.Chrome(options=chrome_options,executable_path=chromeDriver)
bot = browser(driver=driver,DEFAULT_TIMEOUT=20,delay=10)





bot.driver.maximize_window()
bot.get(site)
bot.element('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
bot.click()
bot.element('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
bot.click()


homepage = bot.driver.window_handles[0]
fbPopUp = bot.driver.window_handles[1]

bot.driver.switch_to.window(fbPopUp)

bot.element('//*[@id="email"]')
bot.send(fbuser)
bot.element('//*[@id="pass"]')
bot.send(fbpass)

bot.element('//*[@id="u_0_0"]')
bot.click()

bot.driver.switch_to.window(homepage)

bot.element('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
bot.click()



for i in range(50):
    try:
        sleep(3)
        bot.element('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        bot.click()
        bot.send(Keys.ESCAPE)
    # except :
    #     try :
    #         bot.element('//*[@id="chat-text-area"]')
    #         bot.send('Hey Cutie')
    #         sleep(2)
    #         bot.element('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[4]/button')
    #         bot.click()
    #         sleep(2)
    #     except :
    #         try:
    #             sleep(1)
    #             bot.element('//*[@id="modal-manager"]/div/div/button[2]')
    #             bot.click()
    #         except:
    #             bot.element('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
    #             bot.click()



