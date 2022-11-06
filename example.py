import time

from mypackages import my_crawler,download_pic
"""
url = "https://www.baidu.com/"
xpath = '''//*[@id="hotsearch-content-wrapper"]/li/a/span[2]/text()'''
t1 = time.time()
for text in my_crawler.get_html_by_selenium(url).xpath(xpath):
    print(text)
print(f'运行时间为：{time.time() - t1}s')
"""
url1 = "https://picb8.photophoto.cn/39/463/39463728_1.jpg"
urls = download_pic(url1)
urls.download(name="Test")
