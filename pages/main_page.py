import allure
from locators import *
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Клик на кнопку Конструктор")
    def transition_constructor(self):
        self.click_on_element(MainLocators.order_feed_title_locator)
        self.click_on_element(MainLocators.buns_constructor_locator)


    @allure.step("Клик на кнопку Лента заказов")
    def transition_order_feed(self):
        self.click_on_element(MainLocators.order_feed_title_locator)

    @allure.step("Проверка наличия заголовка Собери бургер")
    def title_constructor(self):
        self.switch_window(MainLocators.title_order_feed, 1)

    @allure.step('Проверка наличия заголовка Лента заказов')
    def title_order_feed(self):
        self.find_element_with_wait(MainLocators.title_order_feed)
        return self.get_text_from_element(MainLocators.title_order_feed)

    @allure.step('Кликаем первый ингредиент на главной странице')
    def click_first_ingredient(self):
        self.click_on_element(MainLocators.first_element)


    @allure.step('Кликаем на крестик у popup с деталями ингридиента')
    def popup_window_closed_clicking_cross(self):
        self.wait_element_clickable(MainLocators.closed_button)
        self.click_on_element(MainLocators.closed_button)


    @allure.step('Кликаем на крестик у popup с информацией о созданном заказе')
    def popup_window_closed_button_order(self):
        self.wait_element_clickable(MainLocators.closed_button_order)
        self.click_on_element(MainLocators.closed_button_order)




    @allure.step('Проверяем виден ли popup')
    def is_element_visible(self):
        return self.element_exist(MainLocators.au)



    @allure.step('Получение значения счетчика ингредиента')
    def value_counter(self):
        return self.get_text_from_element(MainLocators.counter)


    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient(self):
        self.drag_and_drop_on_element(MainLocators.ab, MainLocators.designer)

    @allure.step("Клик на кнопку Оформить заказ")
    def click_make_order(self):
        self.click_on_element(MainLocators.make_order_button)


    @allure.step('Получить номер оформленного заказа')
    def checking_availability_order_number(self):
        return int(self.get_text_from_element(MainLocators.number_order))

    @allure.step('Получить номер оформленного заказа')
    def checking_availability_order_number_1(self):
        return self.get_text_from_element(MainLocators.number_order)
