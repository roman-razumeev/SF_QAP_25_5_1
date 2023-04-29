## Автотест: вход в соцсеть, множественный поиск веб-элементов, обработка полученных результатов. 

Цель: изучение библиотеки Python - &#8220;__Selenium__&#8221; и использования _локаторов веб-элементов_.
### Задание

Написать тест, который проверяет, что на [странице](https://petfriends.skillfactory.ru/my_pets)
со списком питомцев пользователя:
1. Присутствуют все питомцы.
2. Хотя бы у половины питомцев есть фото.
3. У всех питомцев есть имя, возраст и порода.
4. У всех питомцев разные имена.
5. В списке нет повторяющихся питомцев. (Сложное задание)

**Как запускать тесты:**

1) Установить все зависимости:
В командной строке терминала (bash) набрать и выполнить: 
pip install -r requirements.txt
2) Скачать Selenium WebDriver: https://chromedriver.chromium.org/downloads (выбрать совместимую версию с вашим браузером Chrome).
3) Запуск тестов: <BR>
```python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*```<br> 
Примеры запуска:
```
python -m pytest -v --driver Chrome --driver-path D:/chromedriver_win32/chromedriver.exe tests/test_petFriends.py 
python -m pytest -v -s --browser_name=chrome --width_window=1024 --height_window=768 --language=ru --headless=true   tests/test_petFriends.py 
python -m pytest -v -s --browser_name=firefox --width_window=1024 --height_window=768 --language=ru --headless=true   tests/test_petFriends.py 
python -m pytest -v -s --browser_name=firefox --width_window=1024 --height_window=768 --language=ru --headless=false   tests/test_petFriends.py 
```
---
☝️ Пароли спрятаны в файл .env (не выложен здесь). <BR>
Создать в директории проекта файл .env, в него записать: <BR> 
```
valid_email = "ваша учетная запись"
valid_password = "ваш пароль" 
```


