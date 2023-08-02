from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

def register(USER, PASSWORD):
    while True:
        options = webdriver.EdgeOptions()
        # Thêm dòng comment dưới đây nếu bạn muốn trình duyệt hiển thị (không ẩn)
        # options.add_argument('-headless')
        browser = webdriver.Edge(options=options)
        browser.get('https://login.taobao.com/member/login.jhtml')
        user = browser.find_element(By.ID, 'fm-login-id')
        password = browser.find_element(By.ID, 'fm-login-password')
        print(user.is_displayed())
        print(password.is_displayed())
        user.send_keys(USER)
        time.sleep(random.random() * 2)
        password.send_keys(PASSWORD)
        time.sleep(random.random() * 1)
        browser.execute_script("Object.defineProperties(navigator,{webdriver:{get:() => false}})")
        byPass = browser.find_element(By.ID, "nc_1_n1z")
        print(byPass.is_displayed())
        action = ActionChains(browser)
        time.sleep(random.random() * 1)
        # butt = browser.find_element(By.ID, 'nc_1_n1z')
        # browser.switch_to.frame(browser.find_element(By.ID, '_oid_ifr_'))
        # browser.switch_to.default_content()
        # action.click_and_hold(butt).perform()
        action.reset_actions()
        action.move_by_offset(285, 0).perform()
        time.sleep(random.random() * 1)
        # button = browser.find_element(By.CLASS_NAME, '.fm-button fm-submit password-login')
        button = browser.find_element(By.CSS_SELECTOR, '.fm-button.fm-submit.password-login')
        time.sleep(random.random() * 2)
        button.click()
        time.sleep(random.random() * 2)
        cookie = browser.get_cookies()
        cookie_dict = {}
        for cookiez in cookie:
            name = cookiez['name']
            value = cookiez['value']
            cookie_dict[name] = value
        if len(cookie_dict) > 10:
            break
        else:
            browser.quit()
    return cookie_dict

if __name__ == "__main__":
    # Thay đổi USER và PASSWORD bằng thông tin tài khoản của bạn
    USER = "0084818822357"
    PASSWORD = "Aa@123123"
    cookies = register(USER, PASSWORD)
    print(cookies)
