from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def _llegar_al_checkout(page, inventory_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    CartPage(page).go_to_checkout()
    return CheckoutPage(page)


def test_compra_completa(page, inventory_page):
    checkout = _llegar_al_checkout(page, inventory_page)
    checkout.fill_info("Ana", "Pérez", "130001")
    checkout.finish()
    expect(checkout.confirmation).to_have_text("Thank you for your order!")


def test_checkout_sin_nombre_muestra_error(page, inventory_page):
    checkout = _llegar_al_checkout(page, inventory_page)
    checkout.fill_info("", "Pérez", "130001")
    expect(checkout.error).to_contain_text("First Name is required")