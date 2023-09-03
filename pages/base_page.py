import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)
    
    def escrever(self, locator, texto):
        self.encontrar_elemento(locator).send_keys(texto)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento {locator} não existe."

    def verificar_texto_elemento(self, locator, texto):
        assert self.encontrar_elemento(locator).text == texto, f"O texto {texto} não foi encontrado no elemento {locator}."
