from selenium import webdriver
import time
dr = webdriver.Chrome()
dr.maximize_window()
dr.get('https://www.baidu.com/')
dr.find_element_by_xpath('//*[@id="kw"]').send_keys('dddddddddddddddd')
send_kes = dr.find_element_by_xpath('//*[@id="kw"]').get_attribute('value')
key = dr.find_element_by_xpath('//*[@id="su"]').get_attribute('id')
# name = dr.find_element_by_xpath('//*[@id="s-hotsearch-wrapper"]/div/a[1]/div').text
key1 =dr.title
url = dr.current_url
page_source = dr.page_source
print(send_kes)
print(key)
print(key1)
#print(name)
#print(type(name))
print(url)
print(page_source)


'''
获取当前访问页面url　　current_ur
获取当前浏览器标题　　title
获取网页源码　　　　　　　page_source
获取文本内容(既开闭标签之间的内容)　　element.text
获取属性值　　element.get_attribute(value)
获取class属性的值获取元素标签： driver.find_XX().tag_name
'''



time.sleep(5)
dr.quit()
