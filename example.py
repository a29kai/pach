from selenium import webdriver
import time
import json

url = 'https://www.pixiv.net/'

driver = webdriver.Edge()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/106.0.0.0 '
                  'Safari/537.36 Edg/106.0.1370.52 ',
    'referer': 'https://www.pixiv.net/',
    'sec-fetch-site': 'cross-site'

}


def get_cookies():
    # 填写webdriver的保存目录
    # 记得写完整的url 包括http和https
    driver.get(url)
    # 程序打开网页后20秒内 “手动登陆账户”
    time.sleep(20)
    with open('cookies.txt', 'w') as f:
        # 将cookies保存为json格式
        f.write(json.dumps(driver.get_cookies()))


def addcookies():
    # 记得写完整的url 包括http和https
    driver.get(url)
    # 首先清除由于浏览器打开已有的cookies
    driver.delete_all_cookies()
    with open('cookies.txt', 'r') as f:
        # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
        cookies_list = json.load(f)

        # 方法1 将expiry类型变为int
        for cookie in cookies_list:
            # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
    driver.refresh()
    # 方法2删除该字段
    # for cookie in cookieslist:
    #     # 该字段有问题所以删除就可以
    #     if 'expiry' in cookie:
    #         del cookie['expiry']
    #     driver.add_cookie(cookie)


if __name__ == '__main__':
    addcookies()
    url = 'https://www.pixiv.net/artworks/101636493#1'

    driver.get(url)

    click = "/html/body/div[9]/div/div/div/div/div/div/div[2]/div/div[2]/button"
    driver.find_element('xpath', click).click()

    time.sleep(1)
    for page in range(1,12):
        img = f"/html/body/div[8]/div/div/div[1]/div[1]/div[{page}]/a/img"
        img_element = driver.find_element('xpath', img)
        time.sleep(1)
        img_element.screenshot(f"img/test/#Fate/test{page}.png")
        print('over!')
    time.sleep(1)
    driver.close()

