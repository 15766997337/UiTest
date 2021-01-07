#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from tools.find_element import FindElement
import time


class ActionMethod:
    def __init__(self):
        pass

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()

        elif browser == 'firefox':
            self.driver = webdriver.Firefox()

        else:
            self.driver = webdriver.Edge()

        time.sleep(1)

    # 输入地址
    def get_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入元素
    def element_send_keys(self, value, key):

        if ',' in value:
            value = value.split(',')
            key = key.split(',')
            for keys, val in zip(value, key):
                element = self.get_element(val)
                element.send_keys(keys)
                time.sleep(1)
        else:
            element = self.get_element(key)
            element.send_keys(value)
        time.sleep(1)

    # 点击元素
    def click_element(self, key):
        self.get_element(key).click()
        time.sleep(3)

    # 等待
    def sleep_time(self):
        time.sleep(3)

    # 关闭当前窗口
    def close_browser(self):
        self.driver.close()

    # 关闭所有窗口
    def quit_browser(self):
        self.driver.quit()

    # 后退操作
    def back(self):
        self.driver.back()

    # 前进操作
    def forward(self):
        self.driver.forward()

    # 刷新操作
    def refresh(self):
        self.driver.refresh()

    # 清空输入框
    def clear(self, key):
        self.get_element(key).clear()

    # 获取当前访问的网页地址
    def current_url(self):
        return self.driver.current_url

    # 获取 title
    def get_tiele(self):
        return self.driver.title

    # 获取文本内容
    def get_text(self, key):
        text = self.get_element(key).text
        return text

    # 获取输入框内容
    def get_attribute(self, element):
        value = self.get_element(element).get_attribute('value')
        return value


class Judge_method:

    def __init__(self):
        self.action_method = ActionMethod()

    # 判断运行方法
    def run_method(self, method, send_value='', handle_value=''):
        method_value = getattr(self.action_method, method)
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value != '' and handle_value != '':
            result = method_value(send_value, handle_value)
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value()
        return result


a = '1d>11,1d>222,1d>333,1d>333,1d>444'
b = '1d>66,1d>777,1d>888,1d>999,1d>100'
a = a.split(',')
print(type(a))
