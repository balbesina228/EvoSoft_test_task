import random
import time
from io import BytesIO

from PIL import Image
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def click_coordinates(x, y) -> None:
    action = TouchAction(driver)
    action.tap(x=x, y=y).perform()


def get_pixel_color(x, y) -> tuple:
    screenshot = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(screenshot)).convert('RGB')
    pixel_color = image.getpixel((x, y))
    return pixel_color


request = 'How to wash viscose'  # Произвольный запрос, который можно поменять на другой
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'NAME',  # Нужно вставить имя (ID) искомого устройства
    'appPackage': 'com.android.chrome',
    'appActivity': 'com.google.android.apps.chrome.Main'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)
guest_button = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@text, 'Use without an account')]"))
    # При открытии приложения всегда спрашивает, какой аккаунт использовать
)
guest_button.click()
try:
    got_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(@text, 'Got it')]"))  # Иногда появляющееся меню
    )
    got_button.click()
except:
    print('No got_button')
search_field = WebDriverWait(driver, 3).until(
    lambda x: x.find_element(MobileBy.ID, 'com.android.chrome:id/search_box_text')
)
search_field.send_keys(request)  # Ввод запроса
driver.press_keycode(66)  # Enter
time.sleep(5)
actions = TouchAction(driver)
for _ in range(random.randint(3, 10)):
    actions.press(x=500, y=1500).wait(1000).move_to(x=500, y=500).release().perform()  # Листает вниз от 3 до 10 раз

x = 100
y = 100

while True:
    pixel_color = get_pixel_color(x, y)
    if 145 < pixel_color[2] < 225:  # Находит синий цвет ссылки по Blue из RGB
        click_coordinates(x, y)  # Клик по ссылке
        break
    y += 10
    time.sleep(0.1)
time.sleep(5)
driver.back()  # Назад
time.sleep(3)
driver.quit()
