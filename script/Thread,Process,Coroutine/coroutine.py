import random
import asyncio


async def foo(n, name):
    x = 0
    for i in range(n):
        x += random.randint(1,100)
        print(f'{name}:{x}')
        await asyncio.sleep(1)

    return x


t1 = foo(10000, 't1')
t2 = foo(10000, 't2')

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(t1), asyncio.loop]

loop.run_until_complete(asyncio.ensure_future(t2))

# f1, f2 =



