import os
import re
import urllib
from urllib import request, parse


# 设置请求头,请求体
def handle_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    # 根据请求头和请求体穿件请求对象
    req = request.Request(url=url, headers=headers)

    return req


# 用于请求对象发起请求
def request_data(req):
    resp = request.urlopen(req)
    statusCode = resp.getcode()

    return resp.read().decode("utf-8"), statusCode


# 实现业务逻辑
def main():
    # page = 1
    n = 0
    str_target = "Чёртова дюжина"
    url = "http://lj.rossia.org/users/vrotmnen0gi/"
    a = int(input("请输入起始页码："))
    b = int(input("请输入终止页码："))
    print("正在搜索请耐心等待...")
    # 查询主浏览页并,锁定需要查找的人物
    for page in range(a-1, b):
        url = "http://lj.rossia.org/users/vrotmnen0gi/"
        str_mid = "?skip="
        url = url+str_mid+str(page*20)
        # 调用函数获取请求对象
        req = handle_url(url)

        while True:
            try:
                htmlStr1 = request_data(req)[0]
                if request_data(req)[1] == 200:
                    break
            except:
                print("访问失败，重新连接中...")
                print("若多次失败请检查网址格式(提示:网址结尾不能加空格)")

        # 采用正则匹配,获取特定人名的链接
        reg1 = re.compile(str_target+'</td>.*?org/users/vrotmnen0gi/(\d*)\.html#cut',re.S)
        res1 = reg1.findall(htmlStr1)
        page += 1
        netBook = []
        for imageNo in res1:
            head = "http://lj.rossia.org/users/vrotmnen0gi/"
            tail = ".html?mode=reply"
            url_first = head+imageNo+tail
            netBook.append(url_first)
        print(netBook)
        for url_last in netBook:
            try:
                req = handle_url(url_last)
                contend = request_data(req)[0]
                # 匹配特定图片的链接
                reg2 = re.compile('<img border="0" src="(.*?.jpg)')
                res2 = reg2.findall(contend)
                # 逐步遍历访问并保存
                print(res2)
                for j in res2:
                    filename = r"H:\try\\" + str(n) + ".jpg"
                    urllib.request.urlretrieve(url=j, filename=filename)
                    n +=1
                    print("爬取到的图片数量:%d张,请去文件夹查看!" % n)

            except Exception as e:
                print(e)

    print("搜索结束,共%d张!" % n)


if __name__ == "__main__":
    main()


