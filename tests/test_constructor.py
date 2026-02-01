from locators import MainPageLocators
from urls import URLS


class TestConstructorPage:
    def test_transition_to_bun_success(self, driver):
        """Проверка перехода к разделу 'Булки' """
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        driver.find_element(*MainPageLocators.bun_btn).click()
        bun_text = driver.find_element(*MainPageLocators.bun).text                 
        bun_displayed = driver.find_element(*MainPageLocators.bun_ul).is_displayed()

        assert bun_text == 'Булки' and bun_displayed


    def test_transition_to_sauces_success(self, driver):
        """Проверка перехода к разделу 'Соусы' """
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        souces = driver.find_element(*MainPageLocators.sauces).text
        souces_displayed = driver.find_element(*MainPageLocators.sauces_ul).is_displayed()

        assert souces == 'Соусы' and souces_displayed


    def test_transition_to_topping_success(self, driver):
        """Проверка перехода к разделу 'Начинки' """
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.toppings_btn).click()
        topping = driver.find_element(*MainPageLocators.topping).text
        topping_displayed = driver.find_element(*MainPageLocators.topping_ul).is_displayed()

        assert topping == 'Начинки' and topping_displayed
