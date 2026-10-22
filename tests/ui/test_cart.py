from playwright.sync_api import expect


def test_agregar_producto_actualiza_contador(inventory_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    expect(inventory_page.cart_badge).to_have_text("1")


def test_producto_agregado_aparece_en_carrito(page, inventory_page):
    from pages.cart_page import CartPage

    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()

    cart = CartPage(page)
    assert cart.get_item_names() == ["Sauce Labs Backpack"]