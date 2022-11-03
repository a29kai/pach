import time
from lxml import etree
import requests
from selenium import webdriver


class my_crawler:
    """传入url，必要情况下传入新的param，输出经etree处理后的html"""

    @staticmethod
    def get_html_by_requests(url: str, param=None):
        if param is None:
            param = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/106.0.0.0 '
                              'Safari/537.36 Edg/106.0.1370.52 '

            }
        resp = requests.get(url, param)
        html = resp.text
        return etree.HTML(html)

    @staticmethod
    def get_html_by_selenium(url: str):
        # 提前使用selenium包预备爬取js生成数据
        browser = webdriver.Edge()
        # 获取返回值
        browser.get(url)
        time.sleep(1)
        # 获得页面源代码
        html = etree.HTML(browser.page_source)
        browser.close()
        return html
