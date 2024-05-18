from selenium.webdriver.common.by import By


class MainLocators:

    au = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    designer = [By.XPATH, './/section[contains(@class, "BurgerConstructor_basket")]']
    title_first_element = [By.XPATH, '//h2[text()="Детали ингредиента"]']
    closed_button = [By.XPATH, '//button[contains(@class,"close")]']
    ab = [By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']"]
    title_burger = [By.XPATH, ".//*[text()='Соберите бургер']"]
    constructor_title_locator = [By.XPATH, ".//h1[text()='Соберите бургер']"]
    buns_constructor_locator = [By.XPATH, ".//p[text() = 'Конструктор']"]
    title_order_feed = [By.XPATH, ".//h1[text()='Лента заказов']"]
    number_order = [By.XPATH, './/h2[contains(@class, "title_shadow__3ikwq")]']
    first_element = [By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]"]
    counter = [By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]']
    make_order_button = [By.XPATH, '//*[text()="Оформить заказ"]']
    closed_button_order = [By.XPATH, '(.//button[contains(@class, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")])[last()]']
    order_feed_title_locator = [By.XPATH, ".//p[text() = 'Лента Заказов']"]

class OrderLocators:

    title_order_feed = [By.XPATH, ".//h1[text()='Лента заказов']"]
    title_burger = [By.XPATH, ".//*[text()='Соберите бургер']"]
    constructor_title_locator = [By.XPATH, ".//h1[text()='Соберите бургер']"]
    buns_constructor_locator = [By.XPATH, ".//p[text() = 'Конструктор']"]
    title_order_feed = [By.XPATH, ".//h1[text()='Лента заказов']"]
    first_element = [By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]"]

    make_order_button = [By.XPATH, '//*[text()="Оформить заказ"]']
    closed_button_order = [By.XPATH, '(.//button[contains(@class, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")])[last()]']
    closed_button = [By.XPATH, '//button[contains(@class,"close")]']
    au = [By.XPATH, './/h2[text()="Детали ингредиента"]']

    counter = [By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]']
    designer = [By.XPATH, './/section[contains(@class, "BurgerConstructor_basket")]']
    ab = [By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']"]
    order_feed_title_locator = [By.XPATH, ".//p[text() = 'Лента Заказов']"]
    composition_order = [By.XPATH, '//p[text()="Cостав"]']
    first_order = [By.CLASS_NAME, 'OrderHistory_link__1iNby']
    order_done_all_time = [By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[1]']
    order_done_todey = [By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[last()]']
    order_window_open = [By.XPATH, './/div[contains(@class, "Modal_modal_opened__3ISw4")]']
    e_orders_work = [By.XPATH, './/li[text()="Все текущие заказы готовы!"]']
    order_work = [By.XPATH, '(.//ul[contains(@class, "OrderFeed_orderListReady")]/li)[1]']
    closed_button_order = [By.XPATH, '(.//button[contains(@class, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")])[last()]']
    number_order = [By.XPATH, './/h2[contains(@class, "title_shadow__3ikwq")]']


class ProfileLocators:
    profile_button = [By.LINK_TEXT, 'Личный Кабинет']
    title_open_profile = [By.XPATH, '.// h2[text() = "Вход"]']
    email_input = [By.XPATH, './/form//label[text()="Email"]/parent::*/input']
    password_input = [By.XPATH, './/input[@type="password"]']
    button_open_profile = [By.XPATH, '//button[text()= "Войти"]']
    exit_profile_button = [By.XPATH, ".//button[text() = 'Выход']"]
    history_order_button = [By.LINK_TEXT, 'История заказов']
    personal_account_button = [By.LINK_TEXT, 'Личный Кабинет']
    profile_form = [By.XPATH, ".//div[@class = 'Account_account__vgk_w']"]

class PasswordRecoveryeLocators:
    title_open_profile = [By.CLASS_NAME, 'Auth_login__3hAey']
    reset_button = [By.XPATH, './/button[contains(@class, "button_button_size_medium")]']
    reset_password = [By.LINK_TEXT, 'Восстановить пароль']
    reset_password_header = [By.XPATH, './/h2[text()="Восстановление пароля"]']

    secret_key = [By.XPATH, './/label[text()="Введите код из письма"]']
    show_password_button = [By.XPATH, './/div[contains(@class,"icon-action")]']

    login_header = [By.XPATH, './/h2[text()="Вход"]']

    email_input = [By.XPATH, './/label[text()="Email"]/parent::div/input']
    password_input = [By.XPATH, './/label[text()="Пароль"]/parent::div/input']
