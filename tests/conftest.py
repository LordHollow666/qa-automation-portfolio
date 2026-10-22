import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    lp = LoginPage(page)
    lp.open()
    return lp


@pytest.fixture
def inventory_page(page: Page, login_page: LoginPage) -> InventoryPage:
    """Entrega al test ya logueado y viendo el inventario."""
    login_page.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    expect(inventory.title).to_have_text("Products")
    return inventory