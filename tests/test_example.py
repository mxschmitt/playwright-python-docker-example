import re
import playwright
from playwright.sync_api import Page, expect, sync_playwright
import pytest


def test_hello_world():
    assert True


@pytest.fixture()
def context():
    with sync_playwright() as playwright:
        playwright_browser = playwright.chromium.launch(headless=True)
        new_context = playwright_browser.new_context()
        return new_context


def test_example_with_context_fixture(context):
    page = context.new_page()
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.locator("text=Get Started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))


def test_example_with_page_fixture(page: Page):
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.locator("text=Get Started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))