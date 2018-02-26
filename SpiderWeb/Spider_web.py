from selenium import webdriver
import requests
# 模拟登陆
browser = webdriver.Firefox()  # 用火狐驱动 需要geckodriver[注意版本]放到python根目录下
browser.get("https://www.douban.com")  # 请求地址
browser.find_element_by_xpath("//*[@id=\"form_email\"]").send_keys("123456")  # 复制x_path
browser.find_element_by_xpath("//*[@id=\"form_password\"]").send_keys("W@")  # 复制x_path
browser.find_element_by_xpath("//*[@id=\"form_remember\"]").click()  # 点击元素
browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/form/fieldset/div[3]/input").click()

# 爬信息
html = requests.get("https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20")
title = html.json()["subjects"][0]["title"]  # 获取信息的格式

# PyV8 JS加密
