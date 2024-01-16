# 30.3.1 Написать тест, который проверяет, что на странице со списком питомцев пользователя:
# пункт 3: У всех питомцев есть имя, возраст и порода.

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_there_are_a_name_age_and_gender(test_show_my_pets):
    """Поверка, что на странице "Мои питомцы" у всех питомцев есть имя, возраст и порода"""

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    # Сохранение элементов с данными о питомцах в переменную "pet_data"
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Перебираются данные из переменной "pet_data"
    # Сохраняются имя, возраст и порода, остальное меняется на пустую строку и разделяется пробелом
    # Находится количество элементов в получившемся списке и сравнивается с ожидаемым результатом
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        result = len(split_data_pet)
        assert result == 3