import allure
from pages.main_page import MainPage
from data import DataTest
from locators import MainLocators
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage


@allure.feature('Проверка основного функционала')
class TestMainPage:
    @allure.title('Проверка открытия Конструктора по ссылке в шапке сайта')
    def test_click_constructor(self, driver):
        m_page = MainPage(driver)
        m_page.transition_constructor()

        assert m_page.current_url() == DataTest.main_page and m_page.get_title_text() == 'Соберите бургер'

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_order_feed(self, driver):
        m_page = MainPage(driver)
        m_page.transition_order_feed()

        assert m_page.title_order_feed() == 'Лента заказов'

    @allure.title('Проверка появления всплывающего окна с деталями, если кликнуть на ингредиент')
    def test_click_ingridient(self, driver):
        m_page = MainPage(driver)
        m_page.click_first_ingredient()

        assert m_page.get_title_text_detali() == 'Детали ингредиента'

    @allure.title('Проверка возможности закрытия всплывающего окна кликом по крестику')
    def test_popup_window_closed_clicking_cross(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        main_page.popup_window_closed_clicking_cross()

        assert main_page.is_element_visible() is False

    @allure.title('Проверка увеличения счетчика при добавлении этого ингредиента в заказ')
    def test_increasing_ingredient_counter(self, driver):
        m_page = MainPage(driver)
        original_counter = m_page.value_counter()
        m_page.add_ingredient()
        result_counter = m_page.value_counter()

        assert original_counter < result_counter

    @allure.title('Проверка - залогиненный пользователь может оформить заказ.')
    def test_cread_order_with_log_person(self, driver):
        m_page = MainPage(driver)

        profile_page = ProfilePage(driver)
        profile_page.transition_profile()
        profile_page.data_entry_form_auth()
        m_page.add_ingredient()
        order_page = OrderFeedPage(driver)
        order_page.click_make_order()
        assert m_page.checking_availability_order_number() != '0'