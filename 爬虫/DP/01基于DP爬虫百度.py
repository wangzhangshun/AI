# 案例1
from DrissionPage import ChromiumPage,ChromiumOptions

# 1.实例化参数类
co = ChromiumOptions()

# co.headless(False)
co.auto_port()

#2 实例化浏览器引擎
page = ChromiumPage(co)


#3 访问首页
url = "https://www.baidu.com/"
page.get(url)
page.wait.load_start()
page.ele("css:#kw").input("美女")
page.ele("css:#su").click()

print(page.html)

