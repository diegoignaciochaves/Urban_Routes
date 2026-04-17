import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.urban_routes_page import UrbanRoutesPage

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code






class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        def test_full_taxi_order_flow(self):
            self.driver.get(data.urban_routes_url)
            routes_page = UrbanRoutesPage(self.driver)

            # 1. Configurar dirección
            routes_page.set_route(data.address_from, data.address_to)

            # 2. Seleccionar tarifa Comfort
            routes_page.select_comfort_tariff()

            # 3. Rellenar número de teléfono
            routes_page.fill_phone_number(data.phone_number)
            code = retrieve_phone_code(self.driver)
            routes_page.enter_sms_code(code)

            # 4. Agregar tarjeta
            routes_page.add_credit_card(data.card_number, data.card_code)

            # 5. Escribir mensaje al conductor
            routes_page.set_comment(data.message_for_driver)

            # 6. Pedir manta y pañuelos
            routes_page.toggle_blanket_and_handkerchiefs()

            # 7. Pedir 2 helados
            routes_page.add_ice_creams(2)
            assert routes_page.get_ice_cream_count() == "2"

            # 8. Aparece el modal para buscar taxi
            routes_page.click_order_taxi()

            # 9. Opcional: Información del conductor
            assert routes_page.wait_for_driver_info().is_displayed()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
