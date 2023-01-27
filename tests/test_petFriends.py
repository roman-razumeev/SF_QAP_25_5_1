import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password, BASE_URL


class TestPetFriends:


    def setup(self):

        self.url = BASE_URL
        self.user = valid_email
        self.password = valid_password
        self.amount_of_pets = ''  # кол-во питомцев из статистики пользователя
        self.pets_entire_table = []  # список из строк всей таблицы включая
                                     # наименования столбцов и промежутки "*"
        self.images = []   # список со всеми фото питомцев
        self.pets_list = []  # список из строк всей таблицы включая имена
                             # столбцов и промежутки "*"
        self.counter = 0   # счетчик для подсчета питомцев в циклах
        self.pet_names = []  # список из имен
        self.pet_uniq = []  # список уникальных питомцев

        self.login ()
        self.setup_basic_variables ()


    def login(self):
        """Функция для входа на сайт и страницу 'Мои питомцы'. """

        wait = WebDriverWait (pytest.driver, 10)
        pytest.driver.get (self.url + 'login')
        wait.until (EC.presence_of_element_located ((
            By.XPATH, "//input[@id='email']"))).send_keys (self.user)
        wait.until(EC.presence_of_element_located((
            By.XPATH, "//input[@id='pass']"))).send_keys (self.password)
        wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[contains(text(),'Войти')]"))).submit ()
        assert pytest.driver.find_element (By.TAG_NAME, 'h1').text \
               == "PetFriends"
        wait.until(EC.element_to_be_clickable((
            By.XPATH, "//a[contains(text(),'Мои питомцы')]"))).click()


    def setup_basic_variables(self):
        """Функция формирует список в котором оставляет
        только имя, породу, возраст питомцев """

        # Формируем список из строк всей таблицы
        # включая имена столбцов и промежутки '*'
        self.pets_entire_table = pytest.driver.find_elements (
            By.XPATH, '//div[@id="all_my_pets"]')

        # берем все текстовые значения в таблице
        # переводим все в верхний регистр для удобства поиска и
        # формируем список из строк всей таблицы включая имена
        # столбцов и промежутки "*"
        for i in range(len(self.pets_entire_table)):
            self.pets_list = self.pets_entire_table[i].text.upper().split('\n')

        # срезаем нужные, начинаем с 1 и с шагом через одного,
        # оставляя только имя, породу, возраст питомцев
        self.pets_list = self.pets_list[1::2]


    def test_all_pets_are_present(self):
        """Проверяем что на странице со списком моих питомцев
        присутствуют все питомцы"""

        # кол-во питомцев берем из статистики пользователя
        self.amount_of_pets = \
            pytest.driver.find_element (
                By.CSS_SELECTOR, ".\\.col-sm-4.left").text.split (
                '\n')[1].split (" ")[1]

        # проверяем что присутствуют все питомцы
        assert int (self.amount_of_pets) == int (len (self.pets_list))


    def test_half_of_pets_have_photos(self):
        """Поверяем что на странице со списком моих питомцев
        хотя бы у половины питомцев есть фото"""

        # получаем список со всеми фото питомцев
        self.images = pytest.driver.find_elements (By.XPATH, '//tbody//img')

        # в цикле считаем количество питомцев без фото
        for i in range(len(self.images)):
            if self.images[i].get_attribute('src') == '':
                self.counter += 1

        # проверяем количество фото у питомцев в процентах
        assert (round (((self.counter * 100) / int (len(
            self.pets_list))))) \
               <= 50


    def test_all_pets_have_all_fields(self):
        """Поверяем что на странице со списком моих питомцев,
        у всех питомцев есть имя, возраст и порода"""

        # в цикле проверяем что у каждого питомца заполнены все три поля
        for pet in self.pets_list:
            assert len (pet.split (' ')) == 3


    def test_all_pets_have_different_names(self):
        """Поверяем что на странице со списком моих питомцев,
        у всех питомцев разные имена"""

        # цикл формирует список из имен
        for pet in self.pets_list:
            self.pet_names.append (pet.split (' ')[0])

        # проверяем одинаковые имена
        assert len(self.pet_names) == len(set(self.pet_names))


    def test_there_are_no_recurring_pets(self):
        """Поверяем что на странице со списком моих питомцев
        нет повторяющихся питомцев"""

        # цикл формирует список уникальных питомцев
        for pet in self.pets_list:
            if pet in self.pet_uniq:
                continue
            else:
                self.pet_uniq.append (pet)

        # проверяем что нет повторяющихся питомцев
        assert self.pets_list == self.pet_uniq


# pytest -v --driver Chrome --driver-path D:/WebDriver/chromedriver.exe tests/test_petFriends.py
# Если используем синтаксис Selenium_4, то указывать путь до драйвера нет необходимости.
# Драйвер браузеров находится внутри библиотеки Selenium_4
# pytest -v --driver Chrome tests/test_petFriends.py
# pytest -v -s --browser_name=chrome --width_window=1024 --height_window=768 --language=ru --headless=true   tests/test_petFriends.py
# pytest -v -s --browser_name=firefox --width_window=1024 --height_window=768 --language=ru --headless=true   tests/test_petFriends.py
# pytest -v -s --browser_name=firefox --width_window=1024 --height_window=768 --language=ru --headless=false   tests/test_petFriends.py
