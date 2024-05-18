from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Получение текста элемента')
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Ожидание и получение текста элемента')
    def wait_for_element(self, locator):
        self.find_element_located(locator)
        return self.get_text_from_element(locator)

    @allure.step('Ожидание и клик на элемент')
    def find_element_located_click(self, locator):
        self.wait_element_clickable(locator)
        return self.driver.find_element(*locator).click()

    @allure.step('Ожидание и поиск элемента')
    def find_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))


    @allure.step("Получение текущего url")
    def current_url(self):
        return self.driver.current_url

    @allure.step('Вставить текст {text}')
    def find_element_located_input(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)


    def wait_for_invisibility_element(self, locator):
        self.find_element_with_wait(locator).click()



    @allure.step("Получение текста элемента")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text



    @allure.step("Удерживает нажатой левую кнопку мыши на исходном элементе, затем перемещается к целевому смещению и отпускает кнопку мыши.")
    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.find_element_with_wait(locator_one)
        droppable = self.find_element_with_wait(locator_two)
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable, droppable)
        action.perform()


    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click()
        action.perform()

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))

        return self.driver.find_element(*locator)

    def wait_element_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))


    # Проверка отображения элемента
    def check_element(self, locator):
        self.wait_for_load_element(locator)
        return self.driver.find_element(*locator)


    def wait_disappear_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))


    def send_keys(self, locator, key):
        element = self.find_element_with_wait(locator)

        element.send_keys(key)

    def current_url(self):
        return self.driver.current_url

    def get_attribute_value(self, locator, attribute_name: str):
        element = self.find_element_with_wait(locator)
        return element.get_attribute(attribute_name)

    @allure.step('Проверка наличия окна Детали ингредиента')
    def element_exist(self, locator):
        try:
            self.driver.find_element_with_wait(locator)
            return True
        finally:
            return False
