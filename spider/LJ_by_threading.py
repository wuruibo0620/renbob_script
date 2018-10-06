import random
import time
from time import sleep
import requests
from lxml import etree

from threading import Thread
from queue import Queue
import sys


class retry:
    def __int__(self, max_time=3, wait=3, excaptions=(Exception,)):
        self.max_time = max_time
        self.wait = wait
        self.excaptions = excaptions

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.max_time):
                try:
                    res = func(*args, **kwargs)
                except self.excaptions as e:
                    sleep(self.wait)
                    continue
                else:
                    return res

n=10
for i in range(100):
    n += 1
    t = str(int(time.time()))+str(n)
    sleep(0.05)
    if n == 30:
        n =10
    print(t)
