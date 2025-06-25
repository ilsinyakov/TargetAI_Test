from playwright.sync_api import Page


class BasePage:  # noqa: B903
    def __init__(self, page: Page) -> None:
        self.page = page
