from selenium import webdriver
from time import sleep
from Checker import checker
Fb_user = ""
Fb_pass = ""
chromedriverpath = ""
###################################################
# Goto Line 6 and set your Chrome Driver path     #
# exemple : C:\\Users\\Joe\\chromedriver.exe      #
# Goto Line 4 and set your facebook username      #
# Goto line 5 and set your facebook password      #
###################################################


    
class bot():
    def __init__(self):
        if Fb_pass == "" or Fb_user == "" or chromedriverpath == "":
            print("Set FaceBook user name and password to login ! ")
            print("! You should have a Tinder account with Facebook if not create one First")
            
        else:
            self.chrome_options = webdriver.ChromeOptions()
            self.prefs = {"profile.default_content_setting_values.notifications": 2}
            self.chrome_options.add_experimental_option("prefs", self.prefs)
            self.driver = webdriver.Chrome(executable_path=chromedriverpath,options=self.chrome_options)

    def login(self):

        self.driver.maximize_window()
        self.driver.get('https://tinder.com')
        sleep(2)


        loginbtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').text
        if 'PHONE' in loginbtn:
            moreoption = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button').click()
            fblogin = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button').click()
        else:
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').click()
        sleep(2)

        workspace = self.driver.window_handles[0]
        popup = self.driver.window_handles[1]
        self.driver._switch_to.window(popup)

        sleep(2)

        email_fb = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_fb.send_keys(Fb_user)
        passwd_fb = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passwd_fb.send_keys(Fb_pass)

        loing_fb = self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
        sleep(3)

        self.driver.switch_to.window(workspace)

        sleep(2)


    def like(self):

        sleep(2)

        like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like.click()
        sleep(1)
    def dislike(self):

        sleep(2)

        dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike.click()
        sleep(1)

    def sendmsg(self):
        textbox = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
        textbox.send_keys('Hey Cutie')
        sleep(2)
        sendmsg = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button')
        sendmsg.click()
        sleep(2)

    def getimagelink(self):
        sleep(1)
        image = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div/div').get_attribute('style')
        link = image.split("\"")[1]
        return link
    def notintersted(self):
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()



b = bot()
b.login()

for i in range(50):
    try:
        link = b.getimagelink()

        result = checker(link)
        sleep(1)
        print("result ",result)
        if result == 1:
            b.like()
        else:
            b.dislike()

    except :
        try :
            b.sendmsg()
        except :
            b.notintersted()

