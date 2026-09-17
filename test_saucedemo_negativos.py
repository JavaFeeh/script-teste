import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestSauceDemoNegativos(unittest.TestCase):

    def setUp(self):
        self.driver =
webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        
        self.driver.quit()

    
    def test_ct01_login_campos_vazios(self):
        driver = self.driver
        driver.find_element(By.ID, "login-button").click()
        
        mensagem_erro = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Username is required", mensagem_erro)

    
    def test_ct02_login_sem_senha(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "login-button").click()
        
        mensagem_erro = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Password is required", mensagem_erro)

    
    def test_ct03_login_senha_incorreta(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("senha_errada_123")
        driver.find_element(By.ID, "login-button").click()
        
        mensagem_erro = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Username and password do not match", mensagem_erro)

    
    def test_ct04_login_usuario_bloqueado(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        mensagem_erro = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Sorry, this user has been locked out.", mensagem_erro)

    
    def test_ct05_acesso_direto_url(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")
        
        mensagem_erro = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("You can only access '/inventory.html' when you are logged in.", mensagem_erro)

    
    def test_ct06_checkout_campos_vazios(self):
        driver = self.driver
    
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
    
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        
    
        driver.find_element(By.ID, "continue").click()
        
        mensagem_erro = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("First Name is required", mensagem_erro)

    
    def test_ct07_checkout_sem_sobrenome(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        
        driver.find_element(By.ID, "first-name").send_keys("João")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        
    
        elemento_erro = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        )
        
        mensagem_erro = elemento_erro.text
        self.assertIn("Last Name is required", mensagem_erro)

    
    def test_ct08_checkout_sem_cep(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        
        driver.find_element(By.ID, "first-name").send_keys("João")
        driver.find_element(By.ID, "last-name").send_keys("Silva")
        driver.find_element(By.ID, "continue").click()
        
        mensagem_erro = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Postal Code is required", mensagem_erro)

    
    def test_ct10_login_usuario_maiusculo(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("STANDARD_USER")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        mensagem_erro = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Username and password do not match", mensagem_erro)

if __name__ == "__main__":
    unittest.main()
