# coding:utf-8
"""
为了提高系统密集型运算的效率，我们常常会使用到多个进程或者是多个线程，Python中的Threading包实现了线程，multiprocessing
包则实现了多进程。而在3.2版本的python中，将进程与线程进一步封装成concurrent.futures 这个包，使用起来更加方便。
"""
import time
# import requests
import asyncio
import aiohttp

# NUMBERS = range(12)
# URL = 'http://httpbin.org/get?a={}'
#
# # 获取网络请求结果
# def fetch(a):
#     r = requests.get(URL.format(a))
#     return r.json()['args']['a']
#
# # 开始时间
# start = time.time()
#
# for num in NUMBERS:
#     result = fetch(num)
#     print('fetch({}) = {}'.format(num, result))
# # 计算花费的时间
# print('cost time: {}'.format(time.time() - start))

'''
用协程来运行
'''
NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'
async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()
    return data['args']['a']

start = time.time()
loop = asyncio.get_event_loop()
tasks = [fetch_async(num) for num in NUMBERS]
results = loop.run_until_complete(asyncio.gather(*tasks))

for num, results in zip(NUMBERS, results):
    print('fetch({}) = ()'.format(num, results))

print('cost time: {}'.format(time.time() - start))