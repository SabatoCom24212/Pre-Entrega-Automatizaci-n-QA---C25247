"""
- Navegar a la página de login de saucedemo.com
- Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
- Validar login exitoso verificando que se haya redirigido a la página de inventario
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datos.usuario import USUARIO_PRINCIPAL
from utils.locators import USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BUTTON


class TestLogin:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Configuración antes de cada test
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()
    
    def test_login_exitoso_standard_user(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title, "No se cargó la página de login"
        
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, USERNAME_INPUT))
        )
        password_field = wait.until(
            EC.presence_of_element_located((By.ID, PASSWORD_INPUT))
        )
        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, LOGIN_BUTTON))
        )
        
        username_field.send_keys(USUARIO_PRINCIPAL["username"])
        password_field.send_keys(USUARIO_PRINCIPAL["password"])
        login_button.click()
        
        wait.until(EC.url_contains("inventory.html"))
        assert "inventory.html" in driver.current_url, \
            f"No se redirigió a inventory.html. URL actual: {driver.current_url}"
        
        page_title = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )
        assert page_title.text == "Products", \
            f"El título esperado es 'Products', pero se encontró: '{page_title.text}'"
        
        assert "Swag Labs" in driver.title, \
            f"El título del navegador debería contener 'Swag Labs', pero es: {driver.title}"