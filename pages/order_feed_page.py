import allure
from locators import *

from pages.base_page import BasePage


class OrderFeedPage(BasePage):


    @allure.step("Клик на кнопку Лента заказов")
    def transition_order_feed(self):
        self.click_on_element(MainLocators.order_feed_title_locator)

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

