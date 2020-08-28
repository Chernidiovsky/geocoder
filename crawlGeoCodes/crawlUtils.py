# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def utilsBrowser(path):
    """
        需要有chrome浏览器 和 与chrome浏览器版本匹配的chromedriver
        chromedriver链接：https://chromedriver.chromium.org/downloads
    """
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    browser = webdriver.Chrome(chrome_options=option, executable_path=path)
    return browser


def openCrawlUrl(browser, target, interval=10):
    browser.get(target)
    body = BeautifulSoup(browser.page_source, "html.parser").body
    sleep(interval)
    return body