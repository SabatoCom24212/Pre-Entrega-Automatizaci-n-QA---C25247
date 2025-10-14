"""
Funciones auxiliares ("helpers") para los tests
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from datetime import datetime

def esperar_elemento(driver, by, locator, timeout=10):
    """
    Espera explícita hasta que un elemento sea visible
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, locator))
    )

def esperar_url_contiene(driver, texto, timeout=10):
    """
    Espera hasta que la URL contenga un texto específico
    """
    return WebDriverWait(driver, timeout).until(
        EC.url_contains(texto)
    )

def tomar_captura(driver, nombre_archivo):
    """
    Toma una captura de pantalla y la guarda en reports/
    """
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = f"reports/{nombre_archivo}_{timestamp}.png"
    driver.save_screenshot(ruta)
    return ruta

def login(driver, username, password):
    """
    Realiza el proceso de login. El login "en sí" lo testeo en test_login.py. 
    Esta función me sirve para otros tests que requieren estar logueado
    """
    driver.get("https://www.saucedemo.com/")
    
    # Ingresar credenciales
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()