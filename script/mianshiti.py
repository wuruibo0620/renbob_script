prices = {
 'AAPL': 191.88,
 'GOOG': 1186.96,
 'IBM': 149.24,
 'ORCL': 48.44,
 'ACN': 166.89,
 'FB': 208.09,
 'SYMC': 21.29
}

# print(prices.items())
# t = {n:v for v,n in sorted(zip(prices.values(),prices.keys()))}
# print(t)
#
# for v,n in sorted(zip(prices.values(),prices.keys())):
#     print('%s : %d'%(n,v))
#
# print(type(zip(prices.keys(),prices.values())))


from functools import wraps
from random import random
from time import sleep


def retry(*, retry_times=3, max_wait_secs=5, errors=(Exception,)):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retry_times):
               try:
                   return func(*args, **kwargs)
               except errors:
                   sleep(random() * max_wait_secs)
            return None
        return wrapper