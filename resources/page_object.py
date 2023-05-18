from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data_elements.element_mapper import *


class HomePageObject:
    """
        This helps to resolve all actions carried out on the home page
    """

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def launch_page(self, url):
        """
        This method launches the page
        :return: a launched web page
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def mouse_over_element(self, element):
        ele = self.driver.find_element(By.CSS_SELECTOR, element)
        self.action.move_to_element(ele).perform()

    def click_element(self, element):
        self.wait_for_presence(element)
        self.driver.find_element(By.CSS_SELECTOR, element).click()

    def wait_for_presence(self, element):
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def wait_for_selection(self, element):
        self.wait.until(ec.element_located_to_be_selected((By.CSS_SELECTOR, element)))

    def wait_for_text_presence(self, element, text):
        self.wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, element), text))

    def verify_text(self, element, message):
        self.wait_for_presence(element)
        expect_text = self.driver.find_element(By.CSS_SELECTOR, element).text
        assert expect_text == message

    def select_value(self, element, value):
        self.wait_for_presence(element)
        ele = self.driver.find_element(By.CSS_SELECTOR, element)
        select = Select(ele)
        select.select_by_value(value)

    def fill_details(self, field, text):
        self.wait_for_presence(field)
        self.driver.find_element(By.CSS_SELECTOR, field).send_keys(text)

    def execute_click_action(self, element):
        self.wait_for_presence(element)
        ele = self.driver.find_element(By.CSS_SELECTOR, element)
        self.driver.execute_script("arguments[0].click();", ele)


class PageActions(HomePageObject):
    """
        This class has inherited all the attributes of the HomePageObject class
        It can access all the methods.
    """

    def setup(self):
        self.launch_page(HomePage.url)

    def get_product_detail_page(self):
        self.mouse_over_element(HomePage.mens_tab)
        self.mouse_over_element(HomePage.mens_top)
        self.click_element(HomePage.mens_hoodie)

    def select_product(self):
        self.select_value(ShopPage.indexer, '36')
        self.click_element(ShopPage.test_item)
        self.click_element(ShopPage.xl_size)
        self.click_element(ShopPage.orange_colour)
        self.click_element(ShopPage.add_cart_button)
        self.wait_for_text_presence(ShopPage.cart_icon, '1')
        self.click_element(ShopPage.cart_icon)
        self.click_element(ShopPage.checkout_button)

    def fill_payment_details(self):
        self.fill_details(PayDetails.email_field, TestData.email)
        self.fill_details(PayDetails.fname_field, TestData.fname)
        self.fill_details(PayDetails.lname_field, TestData.lname)
        self.fill_details(PayDetails.street_field, TestData.street)
        self.fill_details(PayDetails.city_field, TestData.city)
        self.fill_details(PayDetails.pcode_field, TestData.zip_code)
        self.select_value(PayDetails.country, "NG")
        self.fill_details(PayDetails.region, TestData.state)
        self.fill_details(PayDetails.phone_field, TestData.mobile_number)
        self.wait_for_selection(PayDetails.ship_rate)
        self.click_element(CompleteOrder.continue_button)

    def complete_order(self):
        self.wait_for_text_presence(CompleteOrder.place_holder_for_order, TestData.holder_text)
        self.execute_click_action(CompleteOrder.place_order_button)
        self.wait_for_text_presence(CompleteOrder.success_message_holder, CompleteOrder.actual_success_message)
        self.verify_text(CompleteOrder.success_message_holder, TestData.expected_success_message)

    def open_sauce_demo(self):
        self.launch_page(SauceDemo.url)

    def login_user(self, user):
        self.fill_details(SauceDemo.user_name_field, user)
        self.fill_details(SauceDemo.password_field, TestData.password)
        self.click_element(SauceDemo.login_button)

    def logout(self):
        self.click_element(SauceDemo.burger_menu)
        self.click_element(SauceDemo.logout_link)

