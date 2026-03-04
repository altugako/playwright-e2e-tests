import os
from dotenv import load_dotenv
import pytest
from playwright.async_api import async_playwright

# load environment variables from .env file if present
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

@pytest.fixture(scope="session")
def base_url():
    # you can define BASE_URL in your .env file and use it in tests
    return os.getenv('BASE_URL', 'http://localhost:3000')

# Custom async fixture for browser and page management
@pytest.fixture
async def async_browser():
    """Provide an async browser instance"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        yield browser
        await browser.close()

@pytest.fixture
async def page(async_browser):
    """Provide an async page instance"""
    context = await async_browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()
