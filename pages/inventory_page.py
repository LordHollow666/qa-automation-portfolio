from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_select = page.locator("[data-test='product-sort-container']")
        self.names = page.locator(".inventory_item_name")
        self.prices = page.locator(".inventory_item_price")

    def add_to_cart(self, product_slug: str):
        self.page.locator(f"#add-to-cart-{product_slug}").click()

    def sort_by(self, option: str):
        self.sort_select.select_option(option)

    def get_names(self) -> list[str]:
        return self.names.all_text_contents()

    def get_prices(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.prices.all_text_contents()]

    def open_cart(self):
        self.cart_link.click()