from locators import *
import allure
from data import DataTest
from pages.profile_page import ProfilePage
from pages.password_recovery_page import PasswordRecoveryePage


class TestLoginPage:
    @allure.title('Проверка перехода на форму Восстановление пароля')
    def test_checking_transition_password_recovery_form(self, driver):
        reset_pass_page = PasswordRecoveryePage(driver)

        profile_page = ProfilePage(driver)
        profile_page.transition_profile()
        reset_pass_page.click_on_reset_password()

        assert reset_pass_page.get_text_from_header_reset_password_page() == 'Восстановление пароля'

    @allure.title('Проверка перехода на форму с вводом нового пароля')
    def test_checking_transition_to_form_with_entering_new_password(self, driver):
        reset_pass_page = PasswordRecoveryePage(driver)

        profile_page = ProfilePage(driver)
        profile_page.transition_profile()

        reset_pass_page.click_on_reset_password()
        reset_pass_page.fill_email_field(DataTest.test_email)
        reset_pass_page.click_on_reset_button()

        assert reset_pass_page.return_secret_key_field_text() == 'Введите код из письма'

    @allure.title('Проверка отображения пароля, при нажатии кнопка "Показать пароль" ')
    def test_checking_password_display_when_show_password_button_is_pressed(self, driver):
        reset_pass_page = PasswordRecoveryePage(driver)

        profile_page = ProfilePage(driver)
        profile_page.transition_profile()
        reset_pass_page.click_on_reset_password()
        reset_pass_page.fill_email_field(DataTest.test_email)
        reset_pass_page.click_on_reset_button()
        reset_pass_page.fill_password_field(DataTest.test_password)

        assert reset_pass_page.return_tipe_field() == 'text'