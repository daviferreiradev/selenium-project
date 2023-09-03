from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class LoginPage(BasePage):

    mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//h3[@data-test='error']")

    def fazer_login(self, usuario, senha):
        # self.driver.find_element(*self.username_field).send_keys(usuario)
        # self.driver.find_element(*self.password_field).send_keys(senha)
        # self.driver.find_element(*self.login_button).click()
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def mensagem_erro_login(self):
        self.verificar_elemento_existe(self.error_message_login)

    
