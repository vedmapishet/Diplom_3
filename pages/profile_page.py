import allure
from locators import *
from selenium.common import ElementClickInterceptedException, TimeoutException
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step("Клик на кнопку Личный кабинет")
    def transition_profile(self):

        self.click_on_element(ProfileLocators.profile_button)

    @allure.step("Авторизация")
    def data_entry_form_auth(self, email, password):
        self.find_element_located_input(ProfileLocators.email_input, email)
        self.find_element_located_input(ProfileLocators.password_input, password)
        self.wait_for_invisibility_element(ProfileLocators.button_open_profile)

    @allure.step("Переход в раздел «История заказов»")
    def transition_history_order(self):
        self.wait_element_clickable(ProfileLocators.history_order_button)
        self.click_on_element(ProfileLocators.history_order_button)


    @allure.step("Переход в раздел «Личный кабинет»")
    def transition_personal_accout(self):
        self.wait_for_invisibility_element(ProfileLocators.personal_account_button)


    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_account_button(self):
        try:
            self.click_on_element(ProfileLocators.profile_button)
        except ElementClickInterceptedException:
            self.click_on_element(ProfileLocators.profile_button)

    @allure.step("Выход из профиля")
    def profile_exit(self):
        self.click_on_element(ProfileLocators.exit_profile_button)

    @allure.step('Проверка отображения формы "Личного кабинета"')
    def check_profile_area_form(self):
        return self.check_element(ProfileLocators.profile_form)

