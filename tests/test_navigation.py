"""
- Verificar que el título de la página de inventario sea correcto

- Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
  
- Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datos.usuario import USUARIO_PRINCIPAL
from utils.helpers import login

class TestNavigation:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        login(self.driver, 
              USUARIO_PRINCIPAL["username"], 
              USUARIO_PRINCIPAL["password"])
        
        yield
        self.driver.quit()
    
    def test_titulo_pagina_inventario(self):
        driver = self.driver
        
        assert "inventory.html" in driver.current_url
        
        page_title = driver.find_element(By.CLASS_NAME, "title")
        assert page_title.text == "Products", \
            f"Título incorrecto: {page_title.text}"
    
    def test_productos_visibles(self):
        driver = self.driver
        
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        assert len(productos) > 0, "No se encontraron productos en la página"
    
    def test_primer_producto_detalles(self):
        driver = self.driver
        primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item")
        
        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        
        assert nombre != "", "El nombre del producto está vacío"
        assert precio != "", "El precio del producto está vacío"
        assert "$" in precio, "El precio no tiene formato correcto"
    
    def test_elementos_interfaz_presentes(self):
        driver = self.driver
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed(), "El menú no está visible"
        
        sort_selector = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert sort_selector.is_displayed(), "El selector de orden no está visible"
        
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        assert carrito.is_displayed(), "El carrito no está visible"