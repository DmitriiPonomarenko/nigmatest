import time
from selenium import webdriver
from selenium.webdriver.common.by import By




# options
driver=webdriver.Chrome()

driver.get("https://nigma.science-soft.com/")


def logintest():

    driver.maximize_window()

    login_input = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/label[1]/div/div[1]/div[1]/input")
    login_input.clear()
    login_input.send_keys("dponomarenko")
    time.sleep(1)

    password_input = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/label[2]/div/div/div[1]/input")
    password_input.clear()
    password_input.send_keys("q1w2e3r4")
    time.sleep(1)

    login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button[2]/span[2]")
    login.click()
    time.sleep(1)
    print("Тест авторизации пройден")

    profilepage = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/a/span[2]")
    profilepage.click()
    print("Переход на страницу Пересечение пользователей)")
    time.sleep(5)







if __name__ == '__main__':
    logintest()





