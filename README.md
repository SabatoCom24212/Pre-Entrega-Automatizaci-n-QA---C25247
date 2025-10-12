# Pre-Entrega Automatización QA | C25247

Proyecto de automatización de pruebas para el sitio web [Sauce Demo](https://www.saucedemo.com) utilizando Selenium WebDriver y Python.

---

## Descripción del Proyecto

### Automatización de Login

- Navegar a la página de login de saucedemo.com

- Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")

- Validar login exitoso verificando que se haya redirigido a la página de inventario

---

### Navegación y Verificación del Catálogo

- Verificar que el título de la página de inventario sea correcto

- Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
  
- Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

---

### Interacción con Productos

- Añadir un producto al carrito haciendo clic en el botón correspondiente

- Verificar que el contador del carrito se incremente correctamente

- Navegar al carrito de compras

- Comprobar que el producto añadido aparezca correctamente en el carrito

---

### Funcionalidad Esperada

- Los casos de prueba deben ejecutarse correctamente en el sitio saucedemo.com

- Las validaciones deben ser claras y específicas para cada paso

- El código debe ser legible y estar bien organizado

- Los tests deben ser independientes entre sí (la falla de uno no debe afectar a los demás)

## Instalación

### Prerrequisitos

- Python 3.13.7 instalado
- Google Chrome (última versión)

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Comandos Rápidos

### Ejecutar todos los tests

```bash
pytest tests/ -v
```

### Generar reporte HTML

```bash
pytest tests/ -v --html=reports/reporte.html --self-contained-html
```

### Ver el reporte generado

```bash
# Windows
start reports/reporte.html

```

---

## Dependencias (requirements.txt)

```txt
selenium==4.15.2
pytest==7.4.3
pytest-html==4.1.1
```

---
