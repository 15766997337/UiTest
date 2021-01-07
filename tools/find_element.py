# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from tools.operation_xlsx import OperationExcel


class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    # 判断定位方法
    def get_element(self, data):

        try:
            type = str(data.split('>')[0])
            value = str(data.split('>')[1])
            element = None
            if type == "id":
                element = self.driver.find_element_by_id(value)
            elif type == "name":
                element = self.driver.find_element_by_name(value)
            elif type == "class_name":
                element = self.driver.find_element_by_class_name(value)
            elif type == "tag_name":
                element = self.driver.find_element_by_tag_name(value)
            elif type == "link_text":
                element = self.driver.find_element_by_link_text(value)
            elif type == "partial_link_text":
                element = self.driver.find_element_by_partial_link_text(value)
            elif type == "xpath":
                element = self.driver.find_element_by_xpath(value)
            elif type == "css_selector":
                element = self.driver.find_element_by_css_selector(value)
            return element

        except:

            '''保存截图'''
            # self.driver.save_screenshot(r'C:\Users\Administrator\UI_test\logs\%s.png' %value)
            return None


if __name__ == '__main__':
    driver = webdriver.Chrome()
    i = FindElement(driver)
    i.get_element('id>3')
