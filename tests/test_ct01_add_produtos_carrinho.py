import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_add_produtos_carrinho(self):
        driver = conftest.driver
        # Verifica se o usuário está logado
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Adiciona um produto ao carrinho
        driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
        driver.find_element(By.ID, "shopping_cart_container").click()
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # Compra 1 produto
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Teste")
        driver.find_element(By.ID, "last-name").send_keys("Teste")
        driver.find_element(By.ID, "postal-code").send_keys("00000-000")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()
        assert driver.find_element(By.XPATH, "//h2[text()='Thank you for your order!']").is_displayed()
        driver.find_element(By.ID, "back-to-products").click()

        # # Voltar para a página inicial
        # driver.find_element(By.ID, "shopping_cart_container").click()
        # driver.find_element(By.ID, "continue-shopping").click()

        # Adiciona 2 produtos ao carrinho
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']").click()
        driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
        driver.find_element(By.ID, "shopping_cart_container").click()

        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']").is_displayed()


        # Compra 2 produtos
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Teste")
        driver.find_element(By.ID, "last-name").send_keys("Teste")
        driver.find_element(By.ID, "postal-code").send_keys("00000-000")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()
        assert driver.find_element(By.XPATH, "//h2[text()='Thank you for your order!']").is_displayed()
        driver.find_element(By.ID, "back-to-products").click()

        # Voltar para a página inicial
        driver.find_element(By.ID, "shopping_cart_container").click()
        driver.find_element(By.ID, "continue-shopping").click()
