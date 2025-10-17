"""
- Añadir un producto al carrito haciendo clic en el botón correspondiente

- Verificar que el contador del carrito se incremente correctamente

- Navegar al carrito de compras

- Comprobar que el producto añadido aparezca correctamente en el carrito

"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datos.usuario import USUARIO_PRINCIPAL
from utils.helpers import login

class TestCart:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        # Login automático
        login(self.driver, 
              USUARIO_PRINCIPAL["username"], 
              USUARIO_PRINCIPAL["password"])
        
        yield
        self.driver.quit()
    
    def test_agregar_producto_al_carrito(self):
        """
        Agrega primer producto y verifica item en carrito
        """
        driver = self.driver
        
        try:
            badge_inicial = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            count_inicial = int(badge_inicial.text)
        except:
            count_inicial = 0
        
        boton_agregar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        boton_agregar.click()
        
        badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        count_nuevo = int(badge.text)
        
        assert count_nuevo == count_inicial + 1, \
            f"El contador no se incrementó correctamente. Esperado: {count_inicial + 1}, Actual: {count_nuevo}"
        
        carrito_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        carrito_link.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("cart.html")
        )
        
        items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items_carrito) > 0, "No hay productos en el carrito"
        
        nombre_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert "Backpack" in nombre_en_carrito, \
            f"El producto en el carrito no es el esperado: {nombre_en_carrito}"