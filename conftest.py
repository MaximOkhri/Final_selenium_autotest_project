from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest

def pytest_addoption(parser: Parser):
    parser.addoption("--language", action="store", default="en", help="Choose language")

@pytest.fixture(scope="function")
def browser(request: FixtureRequest):

    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})

    print("\nstart browser for test...")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser...")
    browser.quit()