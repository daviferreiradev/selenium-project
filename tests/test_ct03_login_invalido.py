import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:

    def test_ct03_login_invalido(self):
        # Instanciar páginas
        login_page = LoginPage()

        # Fazer login com usuário inválido
        login_page.fazer_login("standard_user", "senha_invalida")

        # Verificar que o login não foi realizado
        login_page.mensagem_erro_login()
