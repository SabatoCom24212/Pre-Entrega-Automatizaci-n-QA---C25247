"""
Localizadores ("locators") de elementos web
"""

class LoginLocators:
    USERNAME_INPUT = "user-name"
    PASSWORD_INPUT = "password"
    LOGIN_BUTTON = "login-button"
    ERROR_MESSAGE = "error-message-container"

class InventoryLocators:
    PAGE_TITLE = "title"
    PRODUCT_ITEM = "inventory_item"
    PRODUCT_NAME = "inventory_item_name"
    PRODUCT_PRICE = "inventory_item_price"
    PRODUCT_DESCRIPTION = "inventory_item_desc"
    SORT_CONTAINER = "product_sort_container"
    MENU_BUTTON = "react-burger-menu-btn"
    CART_BADGE = "shopping_cart_badge"
    CART_LINK = "shopping_cart_link"
    
class ProductLocators:
    ADD_TO_CART_BACKPACK = "add-to-cart-sauce-labs-backpack"
    ADD_TO_CART_BIKE_LIGHT = "add-to-cart-sauce-labs-bike-light"
    REMOVE_BACKPACK = "remove-sauce-labs-backpack"

class CartLocators:
    CART_ITEM = "cart_item"
    CART_ITEM_NAME = "inventory_item_name"
    CART_ITEM_PRICE = "inventory_item_price"