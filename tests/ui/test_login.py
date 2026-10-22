from playwright.sync_api import Page, expect


def test_login_exitoso(page: Page, login_page):
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_login_usuario_bloqueado(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    login_page.expect_error_contains("locked out")


def test_login_contrasena_incorrecta(login_page):
    login_page.login("standard_user", "clave_mala")
    login_page.expect_error_contains("do not match")