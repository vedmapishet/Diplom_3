import allure
from pages.order_feed_page import OrderFeedPage

from pages.profile_page import ProfilePage


@allure.feature('Проверка Ленты заказов')
class TestOrderFeedPage:
    @allure.title('Проверка возможности открытия всплывающего окна кликом по заказу')
    def test_open_popup_window_with_details(self, driver):
        order_page = OrderFeedPage(driver)
        order_page.transition_order_feed()
        order_page.click_first_feed()
        assert order_page.get_text_composition() == 'Cостав'

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_increasing_order_counter_all_time(self, driver):
        order_page = OrderFeedPage(driver)

        order_page.transition_order_feed()
        one = order_page.value_order_done_all_time()
        profile_page = ProfilePage(driver)
        profile_page.transition_profile()
        profile_page.data_entry_form_auth()
        order_page.transition_order_feed()
        order_page.transition_constructor()
        order_page.add_ingredient()
        order_page.click_make_order()
        order_page.wait_order_placed()
        order_page.popup_window_closed_button_order()
        order_page.transition_order_feed()

        two = order_page.value_order_done_all_time()
        assert int(one) != (int(two) + 1)

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_increasing_order_counter_today(self, driver):
        order_page = OrderFeedPage(driver)
        order_page.transition_order_feed()
        one = order_page.value_order_done_today()
        profile_page = ProfilePage(driver)
        profile_page.transition_profile()
        profile_page.data_entry_form_auth()
        order_page.transition_order_feed()
        order_page.transition_constructor()
        order_page.add_ingredient()
        order_page.click_make_order()
        order_page.wait_order_placed()
        order_page.popup_window_closed_button_order()
        order_page.transition_order_feed()
        order_page.transition_order_feed()
        two = order_page.value_order_done_today()
        assert int(one) != (int(two) + 1)

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_increasing_order_counter_in_work(self, driver):
        order_page = OrderFeedPage(driver)
        profile_page = ProfilePage(driver)
        profile_page.transition_profile()
        profile_page.data_entry_form_auth()
        order_page.transition_order_feed()
        order_page.transition_constructor()
        order_page.add_ingredient()
        order_page.click_make_order()
        order_page.wait_order_placed()
        one = order_page.checking_availability_order_number_1()
        order_page.popup_window_closed_button_order()
        order_page.transition_order_feed()
        order_page.transition_order_feed()
        assert one in order_page.get_orders_in_work()

