from playwright.sync_api import Page, expect


class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(self.URL)

    def login(self, user: str, password: str):
        self.username.fill(user)
        self.password.fill(password)
        self.login_button.click()

    def expect_error_contains(self, text: str):
        expect(self.error).to_contain_text(text)