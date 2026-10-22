from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_names = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("[data-test='checkout']")

    def get_item_names(self) -> list[str]:
        return self.item_names.all_text_contents()

    def go_to_checkout(self):
        self.checkout_button.click()