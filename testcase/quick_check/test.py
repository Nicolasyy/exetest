#!/usr/bin/python2
# coding=utf-8

import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import colors

time_now = time.strftime("%m.%d", time.localtime())
file_1 = open('D:\\click\\parameter.csv', 'r')
list_1 = csv.reader(file_1)
mkpath = "d:\\click\\error\\"
for pars in list_1:
    url = pars[0].decode('gb2312')
    ten_id = pars[1].decode('gb2312')
    username1 = pars[2].decode('gb2312')
    password1 = pars[3].decode('gb2312')
    lang = pars[4].decode('GBK')
    print url, ten_id, username1, password1, lang
    # 干掉谷歌浏览器状态栏提示
    option = webdriver.ChromeOptions()
    option.add_argument("disable-infobars")
    driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(url)
    # 企业ID
    driver.find_element_by_id("txtTenantId").send_keys(ten_id)
    # 账号
    driver.find_element_by_id("txtLoginName").send_keys(username1)
    # 密码
    driver.find_element_by_id("txtPassword").send_keys(password1)
    # 选择语言
    s1 = Select(driver.find_element_by_id('lang'))
    s1.select_by_visible_text(lang)
    # 登录
    time.sleep(1)
    driver.find_element_by_id("btnLogin").click()
    time.sleep(1)
    # 登录页面，登录失败打印提示
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/i/a')
    except:
        print u'登录失败，请重新尝试'
    else:
        print u'登录成功'
    driver.find_elements_by_xpath('//dd[1]/ul[@class="menuson"]/li/a')
    first_list = driver.find_elements_by_xpath('//dd[1]/ul[@class="menuson"]/li/a')
    # 调用函数
    # file_name = mkdir(mkpath)
    # 第一列菜单做特殊处理，单独遍历
    for element_1 in first_list:
        text_1 = element_1.text
        # print text_1
        error_file1 = mkpath + time_now + '.' + ten_id + '.' + text_1 + '.png'
        element_1.click()
        frame_value = driver.find_element_by_id('mainFrame')
        driver.switch_to.frame(frame_value)
        # 获取不到页面元素，抛异常截图
        try:
            aa = driver.find_element_by_xpath('//ul[@class="placeul"]/li[2]/a').text
            if text_1 != aa:
                driver.switch_to.default_content()
                ja = 'window.scroll(0,0)'
                driver.execute_script(ja)
                driver.get_screenshot_as_file(error_file1)
                # print u'\033[31m%s \033[0m不匹配，已截图' %text_1
                # print u'%s' % text_1
                print u'%s不匹配，已截图' % colors.printRed(text_1)
        except:
            driver.switch_to.default_content()
            ja = 'window.scroll(0,0)'
            driver.execute_script(ja)
            driver.get_screenshot_as_file(error_file1)
            # print u'\033[31m%s \033[0m不匹配，已截图' %text_1
            # print u'%s' % text_1
            print u'%s不匹配，已截图' % colors.printRed(text_1)
        driver.switch_to.default_content()
    # 获取菜单
    second_list = driver.find_elements_by_xpath('//dl[@class="leftmenu"]/dd/div')
    for element_2 in second_list[1:]:
        element_2.click()
        time.sleep(1)
        # 获取子菜单
        bb = '//dd/ul[@class="menuson"and@style="display: block;"]/li/a'
        third_list = driver.find_elements_by_xpath(bb)
        for element_3 in third_list:
            # 元素不可见跳过
            # if not element_3.is_displayed():
            #     continue
            text_2 = element_3.text
            # print text_2
            error_file2 = mkpath + time_now + '.' + ten_id + '.' + text_2 + '.png'
            element_3.click()
            frame_value = driver.find_element_by_id('mainFrame')
            driver.switch_to.frame(frame_value)
            # 获取不到页面元素，抛异常截图
            try:
                bb = driver.find_element_by_xpath('//ul[@class="placeul"]/li[2]/a').text
                if text_2 != bb:
                    driver.switch_to.default_content()
                    ja = 'window.scroll(0,0)'
                    driver.execute_script(ja)
                    driver.get_screenshot_as_file(error_file2)
                    # print u'\033[31m%s \033[0m不匹配，已截图' %text_2
                    # print u'%s' % text_2
                    print u'%s不匹配，已截图' % colors.printRed(text_2)
            except:
                driver.switch_to.default_content()
                ja = 'window.scroll(0,0)'
                driver.execute_script(ja)
                driver.get_screenshot_as_file(error_file2)
                # print u'\033[31m%s \033[0m不匹配，已截图' %text_2
                # print u'%s' % text_2
                print u'%s不匹配，已截图' % colors.printRed(text_2)
            driver.switch_to.default_content()
    driver.quit()
    time.sleep(1)
file_1.close()
print u'截图地址为：%s' %mkpath
print 'are you ok?'
raw_input()
