from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"


def test_login_exitoso(page: Page):
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_login_usuario_bloqueado(page: Page):
    page.goto(BASE_URL)
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    expect(page.locator("[data-test='error']")).to_contain_text("locked out")