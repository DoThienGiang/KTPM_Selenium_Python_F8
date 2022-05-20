import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_all_f8(self):
        driver = self.driver
        driver.get("https://www.google.com.vn/?hl=vi")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("f8") #=> tìm từ pycon trong web python.org
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_class_name("LC20lb")
        elem.click()
        self.assertNotIn("No results found.", driver.page_source)
        self.driver.save_screenshot('search_f8_in_gg.png')
        time.sleep(3)    

        username = "username"
        password = "password"
        login = "login"
        elem = driver.find_element_by_class_name("NavBar_loginBtn__5DxZL")
        elem .click()
        elem  = driver.find_element_by_class_name("SigninButton_title__YOCNw")
        elem .click()
        elem  = driver.find_element_by_class_name("FormInput_right__y8Rz2")
        elem .click()
        username = driver.find_elements_by_xpath("//input[@name='email'] ")
        username[0].send_keys("nguyenleanhloan05@gmail.com")   
        password = driver.find_elements_by_xpath("//input[@name='password']")
        password[0].send_keys("loan1971")
        login = driver.find_element_by_class_name("base-module_inner__182n1")
        login.click()
        self.driver.save_screenshot('login_in_F8.png')
        time.sleep(15)

        lotrinh = 'lotrinh'
        khoahoc = 'khoahoc' 
        lotrinh = driver.find_element_by_link_text("Lộ trình")
        lotrinh.click()
        self.driver.save_screenshot('Lo_Trinh.png')
        time.sleep(3)  
        khoahoc = driver.find_element_by_link_text("Học")
        khoahoc.click()
        self.driver.save_screenshot('Hoc.png')
        time.sleep(3)   
        blog = driver.find_element_by_link_text("Blog")
        blog.click()
        self.driver.save_screenshot('Blog.png')
        time.sleep(3) 
        home= driver.find_element_by_link_text("Home")
        home.click()
        self.driver.save_screenshot('Home.png')
        self.assertNotIn("No results found.", driver.page_source)
        self.driver.save_screenshot('Home.png')
        time.sleep(5)  

        elem  = driver.find_element_by_link_text("HTML, CSS từ Zero đến Hero")
        elem.click()
        self.assertNotIn("No results found.", driver.page_source)
        self.driver.save_screenshot('Click_HTML_CSS.png')
        time.sleep(5)   


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()