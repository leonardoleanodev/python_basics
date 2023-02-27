# Example of usage of asyncio

```
In [7]: async def asd():
   ...:     print("start")
   ...:     await asyncio.sleep(1)
   ...:     print("finaly")

In [8]: asyncio.run(asd())
start
finaly

In [9]: async def zxc():
   ...:     print("start")
   ...:     time.sleep(1)
   ...:     print("finaly")

In [10]: asyncio.gather(asd(), asd())
Out[10]: <_GatheringFuture pending>

In [11]: async def main():
    ...:     await asyncio.gather(asd(), asd())

In [12]: asyncio.run(main())
start
start
finaly
finaly

In [13]: async def main():
    ...:     await asyncio.gather(zxc(), zxc())

In [14]: asyncio.run(main())
start
finaly
start
finaly

```
