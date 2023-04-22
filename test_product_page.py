from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
import time

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser: WebDriver, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_messege()
    page.should_be_right_basket_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page. should_be_disappeared()

@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        self.link = self.product.link
        yield
        self.product.delete()

    def test_guest_should_see_login_link_on_product_page(self, browser: WebDriver):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser: WebDriver):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_item()
    basket_page.should_be_empty_basket_message()

@pytest.mark.registred_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser: WebDriver):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser: WebDriver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser: WebDriver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.click_on_add_to_basket_button()
        page.should_be_add_to_basket_messege()
        page.should_be_right_basket_price()