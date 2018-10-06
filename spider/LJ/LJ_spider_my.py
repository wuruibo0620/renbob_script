import random
from threading import Thread, Lock
import queue
import time
import json
from urllib import request


UserAgent_List = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
]


# 全局标识
exit_download_flag = False


# 解析json数据
def parse_json(file_path):
    file = open(file_path, 'r', encoding='utf-8')
    content = json.loads(file.read(), encoding='utf-8', )
    return content


# 定义个一下载爬虫
class DownLoad(Thread):
    def __init__(self, id, url_queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.url_queue = url_queue

    def run(self):
        while True:
            time.sleep(0.1)
            if self.url_queue.empty():
                break
            else:
                dic = self.url_queue.get(block=False)
                url = dic['img_url']
                name = dic['name']

                tc = str(int(time.time()))
                file_name = "H:\\try\\summary1\\" + name + '-' + tc + ".jpg"
                if url is None:
                    continue
                for i in range(2):
                    try:
                        # req = request.Request(url, headers={'item':random.choice(UserAgent_List)})
                        # img = request.urlopen(req).read()
                        img = request.urlopen(url, timeout=20,).read()
                        with open(file_name, 'wb') as fp:
                            fp.write(img)
                            pass
                        print(f'第{self.id}号线程获取到数据{url}')
                        # print(name)
                        break
                    except Exception as e:
                        print(e)
                        time.sleep(1)


# 定义main业务函数
if __name__ == '__main__':
    url_queue = queue.Queue()
    items = parse_json('LJ.json')
    for item in items:
        url_queue.put(item)

    for i in range(5):
        time.sleep(0.3)
        DownLoad(i, url_queue).start()

    exit_download_flag = True
    # print(random.choice(UserAgent_List))
