from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip

def scrapeSol(index, subID, handle):
    s = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service = s)
    driver.implicitly_wait(15)
    
    driver.maximize_window()
    
    # Login
    driver.get("https://codeforces.com/enter")
    driver.find_element(By.ID, "handleOrEmail").send_keys("anhbqtq@gmail.com")
    driver.find_element(By.ID, "password").send_keys("buiquocanh123")
    driver.find_element(By.CLASS_NAME, "submit").click()
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logout')]")))

    subLink = "https://codeforces.com/group/pzborSva9T/contest/413925/submission/" + str(subID)
    driver.get(subLink)
    driver.find_element(By.CLASS_NAME, "source-copier").click()


    fileName = "\\" + str(index) + "_" + str(subID) + "_" + str(handle)
    probIndex = "\\" + str(index)
    path = "C:\\Users\\Computer\\Dropbox\\PC\\Desktop\\NITC\\Plagiarism_Detector\\FINAL" + str(probIndex) + str(fileName) + ".txt"
    textFile = open(path, "w")

    finalSubmit = pyperclip.paste()

    textFile.write(finalSubmit)

    textFile.close()

    driver.close()