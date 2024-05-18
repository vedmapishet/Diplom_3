import allure
from pages.profile_page import ProfilePage

from locators import *



@allure.feature('Проверка личного кабинета')
class TestProfilePage:


    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_click_profile(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.transition_profile()
        assert 'login' in profile_page.current_url() and profile_page.get_title_text_open() == 'Вход'

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_transition_order_history(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.transition_profile()
        profile_page.data_entry_form_auth()
        profile_page.transition_profile()
        profile_page.transition_history_order()
        assert 'order-history' in profile_page.current_url()

    @allure.title('Проверка Выхода из «Личного кабинета»')
    def test_exit_profile(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.transition_profile()
        profile_page.data_entry_form_auth()
        profile_page.click_on_account_button()
        profile_page.check_profile_area_form()
        profile_page.profile_exit()
        assert profile_page.get_title_text_open() and 'login' in profile_page.current_url()
