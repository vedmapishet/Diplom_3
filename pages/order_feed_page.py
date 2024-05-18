import allure
from locators import *

from pages.base_page import BasePage


class OrderFeedPage(BasePage):


    @allure.step("Клик на заказ")
    def click_first_feed(self):
        self.click_on_element(OrderLocators.first_order)

    @allure.step('Получение значения счетчика заказа за все время')
    def value_order_done_all_time(self):
        self.wait_element_clickable(OrderLocators.order_done_all_time)
        return self.get_text_from_element(OrderLocators.order_done_all_time)

    @allure.step('Получение значения счетчика заказа за все время')
    def value_order_done_today(self):
        self.wait_element_clickable(OrderLocators.order_done_todey)
        return self.get_text_from_element(OrderLocators.order_done_todey)

    @allure.step('Проверка открыто ли окно заказа')
    def order_window_open(self):
        element = self.get_attribute_value(OrderLocators.order_window_open, 'class')
        if 'opened' in element:
            return True
        else:
            return False

    @allure.step('Получить список заказов в работе')
    def get_orders_in_work(self):
        self.find_element_with_wait(OrderLocators.e_orders_work)
        self.wait_disappear_element(OrderLocators.e_orders_work)
        return self.get_text_from_element(OrderLocators.order_work)

    @allure.step('Ожидание формирования номера заказа')
    def wait_order_placed(self):

        self.find_element_with_wait(OrderLocators.order_window_open)
        self.wait_disappear_element(OrderLocators.order_window_open)

    @allure.step('Получить текст Состав')
    def get_text_composition(self):
        return self.wait_for_element(OrderLocators.composition_order)

    @allure.step('Кликаем на крестик у popup с информацией о созданном заказе')
    def popup_window_closed_button_order(self):
        self.wait_element_clickable(OrderLocators.closed_button_order)
        self.click_on_element(OrderLocators.closed_button_order)


    @allure.step("Клик на кнопку Оформить заказ")
    def click_make_order(self):
        self.click_on_element(OrderLocators.make_order_button)


    @allure.step("Проверка наличия заголовка Собери бургер")
    def title_constructor(self):
        self.switch_window(OrderLocators.title_order_feed, 1)

    @allure.step("Клик на кнопку Конструктор")
    def transition_constructor(self):
        self.click_on_element(OrderLocators.order_feed_title_locator)
        self.click_on_element(OrderLocators.buns_constructor_locator)

    @allure.step('Проверка наличия заголовка Лента заказов')
    def title_order_feed(self):
        self.find_element_with_wait(OrderLocators.title_order_feed)
        return self.get_text_from_element(OrderLocators.title_order_feed)

    @allure.step('Кликаем первый ингредиент на главной странице')
    def click_first_ingredient(self):
        self.click_on_element(MainLocators.first_element)

    @allure.step('Кликаем на крестик у popup с деталями ингридиента')
    def popup_window_closed_clicking_cross(self):
        self.wait_element_clickable(OrderLocators.closed_button)
        self.click_on_element(OrderLocators.closed_button)

    @allure.step('Проверяем виден ли popup')
    def is_element_visible(self):
        return self.element_exist(OrderLocators.au)

    @allure.step('Получение значения счетчика ингредиента')
    def value_counter(self):
        return self.get_text_from_element(OrderLocators.counter)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient(self):
        self.drag_and_drop_on_element(OrderLocators.ab, OrderLocators.designer)

    @allure.step('Получить номер оформленного заказа')
    def checking_availability_order_number_1(self):
        return self.get_text_from_element(OrderLocators.number_order)

    @allure.step("Клик на кнопку Лента заказов")
    def transition_order_feed(self):
        self.click_on_element(OrderLocators.order_feed_title_locator)




