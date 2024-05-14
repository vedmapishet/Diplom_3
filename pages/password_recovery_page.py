import allure
from locators import *
from pages.base_page import BasePage


class PasswordRecoveryePage(BasePage):
    @allure.step('Заполнить поле email')
    def fill_email_field(self, email):
        self.send_keys(LoginLocators.email_input, email)

    @allure.step('Заполнить поле пароль')
    def fill_password_field(self, password):
        self.send_keys(LoginLocators.password_input, password)

    @allure.step('Нажать на кнопку Восстановить пароль')
    def click_on_reset_button(self):
        self.click_on_element(PasswordRecoveryeLocators.reset_button)

    @allure.step('Нажать на ссылку для перехода на форму восстановления пароля')
    def click_on_reset_password(self):
        self.wait_element_clickable(PasswordRecoveryeLocators.reset_password)
        self.click_on_element(PasswordRecoveryeLocators.reset_password)

    @allure.step('Получить заголовок формы восстановления пароля')
    def get_text_from_header_reset_password_page(self):
        self.find_element_with_wait(PasswordRecoveryeLocators.reset_password_header)
        return self.get_text_from_element(PasswordRecoveryeLocators.reset_password_header)

    @allure.step('Получить текст в поле "введите код из письма"')
    def return_secret_key_field_text(self):
        return self.get_text_from_element(PasswordRecoveryeLocators.secret_key)

    @allure.step('Вернуть тип поля, в которое введен пароль')
    def return_tipe_field(self):
        self.click_on_element(PasswordRecoveryeLocators.show_password_button)
        return self.get_attribute_value(LoginLocators.password_input, 'type')