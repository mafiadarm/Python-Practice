#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           06_24_2018  15:24
  File Name:      /GitHub/selenium_for_firefox
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  pip install selenium
  官方文档http://selenium-python.readthedocs.io/index.html
  chromedriver下载地址https://sites.google.com/a/chromium.org/chromedriver/downloads
  chromedriver下载地址http://chromedriver.storage.googleapis.com/index.html

  firefoxdriver下载地址https://github.com/mozilla/geckodriver/releases/
  firefoxdriver下载地址http://ftp.mozilla.org/pub/firefox/releases/

  使用无界面浏览器进行获取，通过selenium进行调用
  driver要和实际使用的浏览器版本对应
  phantomjs已经停更，但是可以使用

  大部分网站使用ajx加载会稍微慢一点，所以会有等待产生，
  当没有等待的时候，元素就会搜索不到
  使用WebDriverWait去做检查元素出现的等待
==============================
"""
import random
import time

__author__ = 'Loffew'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 用于拖拽的鼠标动作
from selenium.webdriver.support.wait import WebDriverWait  # 用于自动等待加载完毕
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  # 用来做PHANTOMJS配置


def firefox():
    # 用geckodriver.exe做测试，放在python根目录下
    driver = webdriver.Firefox()

    driver.get("https://www.baidu.com")  # 获取实际代码，相当于是审查元素
    try:
        # driver.save_screenshot("test.png")  # 对当前屏幕截图
        # driver.find_element_by_id("kw")  # 对id进行定位
        # driver.find_element_by_id("kw").send_keys("python")  # 对id进行定位并输入字符串
        # driver.find_element_by_class_name()
        driver.find_element_by_link_text("贴吧").click()
        # driver.find_element_by_xpath()
        # driver.find_element_by_css_selector()
    finally:
        driver.close()  # 浏览器不会自动关闭，必须要手动关闭


def changewindow():
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")
    try:
        driver.find_element_by_id("kw").send_keys("python")
        driver.find_element_by_id("su").click()
        time.sleep(5)  # 要等加载出来
        driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
        driver.switch_to_window("Python（计算机程序设计语言）_百度百科")  # 切换到窗口去
        """
        driver.switch_to_alert()  # 切换到弹窗上去
        time.sleep(3)
        driver.accept()
        """
    finally:
        time.sleep(4)
        driver.close()


def get_cookies():
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")
    try:
        driver.find_element_by_id("kw").send_keys("python")  # 这里假比是模拟登陆以后
        cookies = {}
        for item in driver.get_cookies():
            cookies[item.get("name")] = item.get["value"]
        return cookies  # 直接的cookies字典，可以传到requests里面去
    finally:
        time.sleep(4)
        driver.close()


def drag():
    """
    ActionChains提供的方法
        ActionChains(driver).click()  # 单击鼠标左键
        ActionChains(driver).click_and_hold(on_element=None)  # 按住鼠标左键不放
        ActionChains(driver).context_click(on_element=None)  # 单击鼠标右键
        ActionChains(driver).double_click(on_element=None)  # 双击鼠标左键
        ActionChains(driver).drag_and_drop(source, target)  # 从一个元素位置拖到另一个元素位置
        ActionChains(driver).drag_and_drop_by_offset(source, xoffset, yoffset)  # 拖到某个坐标然后松开
        ActionChains(driver).move_by_offset(xoffset, yoffset)  # 鼠标移动到距离当前位置
        ActionChains(driver).move_to_element(to_element)  # 鼠标移动到某个元素
        ActionChains(driver).move_to_element_with_offset(to_element, xoffset, yoffset)  # 讲鼠标移动到距离某元素某个距离的位置
        ActionChains(driver).release(on_element=None)  # 在某个元素位置松开鼠标左键
        .perform()  # 执行链中的所有动作
    """
    driver = webdriver.Firefox()
    driver.get("http://www.treejs.cn/v3/demo/cn/exedit/drag.html")
    try:
        time.sleep(2)
        element = driver.find_element_by_id("treeDemo_2_span")  # 定位起始位置
        target = driver.find_element_by_id("treeDemo_3_span")  # 定位目标位置
        ActionChains(driver).drag_and_drop(element, target).perform()  # 拖拽到某个元素然后松开
    finally:
        time.sleep(4)
        driver.close()


def wait_load():
    """
    显式等待
    EC 的判断条件
        title_is  精准验证title
        title_contains  验证title内容

        presence_of_element_located  符合条件的元素一出现就下一步
        presence_of_all_element_located  符合条件的元素出现再下一步

        visibility_of_element_located  验证元素可见，传入tuple
        invisibility_of_element_located  验证元素
        visibility_of  验证元素可见，传入WebElement

        text_to_be_present_in_element  判断元素的text是否出现
        text_to_be_present_in_element_value  判断元素的value是否出现

        frame_to_be_available_and_switch_to_it  判断frame是否可切入，可传入locator元素或者直接传入定位方式：id、name、index或WebElement

        alert_is_present  判断是否有alert出现

        element_to_be_clickable  判断元素是否可点击，传入locator
    """
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")
    try:
        # 给出某个元素是否已经出现 可以多个关键词(接收的是tuple)
        element = (By.LINK_TEXT, "贴吧")
        # 等待环境加载20秒钟，每0.5秒检查一次，直到element元素出现，超时返回报错
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_all_elements_located(element))
        # 定位“贴吧”元素，获取href属性，打印出来
        print(driver.find_element_by_link_text("贴吧").get_attribute("href"))
    finally:
        time.sleep(4)
        driver.close()

    """
    隐性等待
    当加载成功，则直接进入下一步，如果没成功会一直等到时间到了，然后进入下一步
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get("https://www.baidu.com")


def phantomjs_web():
    """
    phantomjs.exe最好配置一个环境变量，否则必须再驱动的第一个参数填入路径
    http://phantomjs.org/download.html从官网下载，放到python路径下
    3.8.1版本会有警告提示：selenium已经放弃phantomjs了，用低版本的不会警告

    # 实例化
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    # 从user_agents列表随机选一个浏览器头 USER_AGENTS为头信息的列表
    dcap["phantomjs.page.settings.userAgent"] = (random.choice(USER_AGENTS))
    # 不加载图片，可以加快速度
    dcap["phantomjs.page.settings.loadImages"] = False
    # 设置代理
    service_args = ["--proxy=127.0.0.1:9999", "--proxy-type=socks5"]
    # 打开带配置信息的phantomJS 如果phantomJS设置过环境变量phantomjs_driver_path可以不写
    driver = webdriver.PhantomJS(phantomjs_driver_path, desired_capabilities=dcap, server_args=service_args)
    """
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = "UA"
    dcap["phantomjs.page.settings.loadImages"] = False
    driver = webdriver.PhantomJS(desired_capabilities=dcap, )
    driver.get("https://www.baidu.com")
    print(driver.title)


def test163():
    """
    163邮箱就要用到iframe,切入的时候，如果没有id或者name标签，可以直接使用索引进行切入，特别是在有多少个嵌入式的时候
    :return:
    """
    driver = webdriver.Firefox()
    driver.get("https://email.163.com/")

    element = (By.ID, 'panel-163')
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_all_elements_located(element))
    print("get id='panel-163'")

    iframe = driver.find_element_by_xpath('//*[@id="panel-163"]/iframe').get_property('id')
    # driver.switch_to.frame(0)  # 直接用索引也可以切进去
    driver.switch_to.frame(iframe)
    print("switch seccess")
    # print(driver.page_source)

    element = (By.ID, "account-box")
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_all_elements_located(element))

    driver.find_element_by_xpath('//*[@id="account-box"]/div/input').send_keys("123")
    # print(driver.find_element_by_xpath('//*[@class="m-container"]/*/*/input[@name="password"]').get_property("name"))
    driver.find_element_by_xpath('//*[@class="m-container"]/*/*/input[@name="password"]').send_keys("123456")

    driver.switch_to.default_content()
    driver.close()


if __name__ == '__main__':
    # firefox()
    # changewindow()
    # get_cookies()
    # drag()
    # wait_load()
    # phantomjs_web()
    test163()

