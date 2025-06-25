from collections.abc import Generator

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Browser, Page, sync_playwright


@pytest.fixture(scope="session", autouse=True)
def load_env() -> None:
    load_dotenv()


@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser) -> Generator[Page, None, None]:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
