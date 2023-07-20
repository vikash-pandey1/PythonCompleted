import time
import asyncio
import requests

async def fun():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram1.ico","wb").write(response.content)
    print("fuc 1")
    return "vikash"
async def fun2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram2.ico","wb").write(response.content)
    print("fuc 1")
async def fun3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram3.ico","wb").write(response.content)
    print("fuc 1")
async def main():
    L = await asyncio.gather(
        fun(),
        fun2(),
        fun3(),
    )
    print(L)
    # task = asyncio.create_task(fun())
    # await fun2()
    # await fun3()
asyncio.run(main())