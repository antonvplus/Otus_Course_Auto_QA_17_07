from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from faker import Faker
import random
import logging
import allure

class RegistrationPage(BasePage):

    FIRST_NAME = (By.ID, 'field-firstname')
    LAST_NAME = (By.ID, 'field-lastname')
    EMAIL = (By.ID, 'field-email')
    PASSWORD = (By.ID, 'field-password')
    BIRTHDATE = (By.ID, 'field-birthday')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'footer > button')
    CHECK_BUTTON_I_AGREE = (By.CSS_SELECTOR, 'input[name="psgdpr"]')
    CHECK_BUTTON_CUSTOMER_DATA_PRIVACY = (By.CSS_SELECTOR, 'input[name="customer_privacy"]')
    USER = (By.CSS_SELECTOR, "#_desktop_user_info > div > a.account > span")

    dict_elements_on_page = {'first_name': FIRST_NAME,
                             'last_name': LAST_NAME,
                             'email': EMAIL,
                             'password': PASSWORD,
                             'birthdate': BIRTHDATE,
                             'save_button': SAVE_BUTTON}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("Logger.RegistrationPage")

    def open(self) -> None:
        self.logger.info(f"Открыт браузер: {self.url}")
        super().open()

    def check_clickable_element(self, element: str) -> None:
        self.logger.info(f"Проверка, что элемент {element} кликабельный")
        assert self.is_element_clickable(self.dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        self.logger.info(f"Проверка, что элемент {element} отображается на странице")
        assert self.is_element_present(self.dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

    def fill_in_all_fields(self) -> tuple[str, str]:
        fake = Faker('en_US')
        with allure.step("Заполняем поле имя"):
            self.logger.info("Заполнение поля имя")
            name = fake.name()
            self.fill_in_text_field(self.FIRST_NAME, name)
        with allure.step("Заполняем поле фамилия"):
            self.logger.info("Заполнение поля фамилия")
            last_name = fake.last_name()
            self.fill_in_text_field(self.LAST_NAME, last_name)
        with allure.step("Заполняем поле email"):
            self.logger.info("Заполнение поля email")
            self.fill_in_text_field(self.EMAIL, fake.email())
        with allure.step("Заполняем поле пароль"):
            self.logger.info("Заполнение поля пароль")
            self.fill_in_text_field(self.PASSWORD, fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
        with allure.step("Заполняем поле день рождения"):
            self.logger.info("Заполнение поля день рождение")
            self.fill_in_text_field(self.BIRTHDATE, f"{random.randint(1,12)}/{random.randint(1,28)}/{random.randint(1970, 2000)}")
        with allure.step("Выбираем чекбоксы"):
            self.logger.info("Клик на чекбоксы")
            self.click_on_checkbox(self.CHECK_BUTTON_I_AGREE)
            self.click_on_checkbox(self.CHECK_BUTTON_CUSTOMER_DATA_PRIVACY)
        with allure.step("Сохраняем"):
            self.logger.info("Сохранить")
            self.click_on_element(self.SAVE_BUTTON)
        return name, last_name

    @allure.step("Выполняем проверку нового юзера")
    def check_new_user(self, name: str, last_name: str) -> None:
        user = self.get_text_element(self.USER)
        self.logger.info(f"Проверка, что пользователь {user} отображается на странице")
        assert user == f"{name} {last_name}", ("The names don't match: "
                                               f"Expect for a user named: '{name} {last_name}'"
                                               f"The user name is displayed: '{user}'")
