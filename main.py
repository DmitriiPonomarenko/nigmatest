import time

from selenium import webdriver
from selenium.webdriver.common.by import By



# options
options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

url = "http://83.137.53.46:82/"
driver = webdriver.Chrome(
    executable_path="/Users/Dmitriy/PycharmProjects/nigmatest/chromedriver/chromedriver.exe",
    options=options
)

def logintest():
    driver.get(url=url)
    driver.maximize_window()

    login_input = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/label[1]/div/div[1]/div[1]/input")
    login_input.clear()
    login_input.send_keys("admin")
    time.sleep(1)

    password_input = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/label[2]/div/div/div[1]/input")
    password_input.clear()
    password_input.send_keys("q1w2e3r4")
    time.sleep(1)

    login = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[2]/button[1]")
    login.click()
    time.sleep(1)
    print("Тест авторизации пройден (Пуш с мака ")

    profilepage = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/a/span[2]")
    profilepage.click()
    print("Переход на страницу Цифровой профиль выполнен )")
    time.sleep(5)

    mainpage = driver.find_element(By.XPATH, "/html/body/div/div/header/div[1]/div[1]/a")
    mainpage.click()
    print("Переход на главную страницу")
    time.sleep(2)

    intersectionpage = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/a/span[2]")
    intersectionpage.click()
    print("Переход на страницу пересечений")
    time.sleep(5)


    mainpage.click()
    print("Переход на главную")
    time.sleep(2)

    intersectionpage = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/a/span[2]")
    intersectionpage.click()
    print("Переход на страницу Сегментации аудитории")
    time.sleep(5)

    mainpage.click()
    print("Переход на главную")
    time.sleep(2)

    intersectionpage = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[4]/div/div[1]/div/div[2]/a/span[2]")
    intersectionpage.click()
    print("Переход на страницу Системные пользователи")
    time.sleep(5)

    mainpage.click()
    print("Переход на главную")
    time.sleep(2)







if __name__ == '__main__':
    logintest()





