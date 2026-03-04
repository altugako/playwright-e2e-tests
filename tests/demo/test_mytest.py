from playwright.async_api import Page, expect
import pytest
import re

@pytest.mark.e2e
@pytest.mark.asyncio
async def test_should_load_home_page_with_correct_title(page: Page) -> None:
    # Go to the home page
    await page.goto("https://katalon-demo-cura.herokuapp.com/")

    # Assert if the title is correct
    await expect(page).to_have_title(re.compile(r"CURA Healthcare Service"))

    # Assert header text
    await expect(page.locator('//h1')).to_have_text('CURA Healthcare Service')
