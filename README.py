# Urban Routes Automation Project

## Descripción
Este proyecto consiste en una suite de pruebas automatizadas para la aplicación web **Urban Routes**. El objetivo es validar el flujo completo de usuario al solicitar un servicio de taxi, asegurando que funciones críticas como la selección de tarifas, registro de teléfono, vinculación de métodos de pago y selección de servicios adicionales operen correctamente.

## Tecnologías y Técnicas
- **Lenguaje:** Python 3.x
- **Framework de Pruebas:** Pytest
- **Automatización del Navegador:** Selenium WebDriver
- **Patrón de Diseño:** Page Object Model (POM) para separar la lógica de los elementos de la interfaz de las pruebas.
- **Manejo de Esperas:** Explicit Waits para gestionar la carga dinámica de elementos.
- **Captura de Logs:** Uso de Chrome DevTools Protocol para interceptar códigos SMS de confirmación.

## Instrucciones de Ejecución
1.  **Clonar el repositorio** o descargar los archivos del proyecto.
2.  **Instalar dependencias:**
    Asegúrate de tener instalado Selenium y Pytest:
    ```bash
    pip install selenium pytest
    ```
3.  **Configurar WebDriver:**
    Asegúrate de tener el `chromedriver` compatible con tu versión de Chrome instalado en tu sistema.
4.  **Actualizar Datos:**
    Verifica que el archivo `data.py` contenga la URL actualizada generada por el servidor.
5.  **Ejecutar las pruebas:**
    Desde la terminal, en la raíz del proyecto, ejecuta:
    ```bash
    pytest main.py
    ```