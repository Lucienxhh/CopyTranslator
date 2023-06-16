from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))      # setting BASE_DIR as directory name where current file resides 
chrome_path = BASE_DIR + '\Application\chrome.exe'         # setting chrome_path as the path of Chrome browser 
driver_path = BASE_DIR + '\Application\chromedriver.exe'   # setting driver_path as the path of chromedriver executable

class Translator():
    # Initializes the Translator class
    def __init__(self, core="baidu", headless=False, refresh_time=8, refresh_rate=0.5):
        options = ChromeOptions()
        options.binary_location = chrome_path
        
        # adding the option to run Chrome in headless mode
        if headless:       
            options.add_argument("--headless")  
        
        self.refresh_time = refresh_time
        self.refresh_rate = refresh_rate
        self.request = 0

        # reduce the possibility of someone trying to detect that this instance is being automated
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        
        # initializing the Chrome WebDriver with options and executable path specified
        # work with Selenium < 4.0
        self.driver = Chrome(executable_path=driver_path, chrome_options=options)
        
        self.setCore(core)
        self.driver.get(self.url)
        
        sleep(1)
        self.refresh()
    
    # Sets the translation service provider and its corresponding configuration
    def setCore(self, translator_core):
        if translator_core == "baidu":
            self.url = "https://fanyi.baidu.com/#en/zh/"
            self.input_path = (By.ID, "baidu_translate_input")
            self.output_path = (By.CLASS_NAME, "output-bd") 
        
        elif translator_core == "google":
            self.url = "https://translate.google.cn/?sl=auto&tl=zh-CN"
            self.input_path = (By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
            self.output_path = (By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span/span")
     
    # Destroys the Translator class
    def close(self):
        self.driver.quit()
        print("driver is free")
    
    # Enters text into the input field of the translation website
    def setInput(self, text):
        input = self.driver.find_element(*self.input_path)
        input.clear()
        input.send_keys(text)
        input.send_keys(Keys.ENTER)
        
    # Gets the translated text from the output field of the translation website.
    def getOutput(self):
        try:
            output = self.driver.find_element(*self.output_path).text
        except Exception:
            output = "fails to translate it"
        
        self.refresh()
        return output
    
    # Refreshes the translation website
    def refresh(self):
        if self.request % self.refresh_rate == 0:
            self.driver.refresh()
            self.request = 0
        sleep(self.refresh_time)
    
    # Checks if the element exists in the DOM of the translation website
    def isElementExists(self, ele):
        try:
            self.driver.find_element(ele)
            return True
        except Exception:
            return False

    # translate English to Chinese or Chinese to English
    def translate(self, text):
        if self.isElementExists(self.output_path):
            old_tran = self.getOutput()
        else:
            old_tran = ""
        self.setInput(text)
        waitTime = len(text) / 800 + 1
        sleep(waitTime)
        new_tran = self.getOutput()
        while new_tran == old_tran:
            new_tran = self.getOutput()
            sleep(0.3)
        return new_tran

# for test
if __name__ == "__main__":
    tran = Translator("baidu")
    tran.translate("this is a test")