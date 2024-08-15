import asyncio
import time
from functools import wraps, partial


def to_async(func):
    # Makes sure that function is returned for e.g. func.__name__ etc.
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()  # Make event loop of nothing exists
        # Return function with variables (event) filled in
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run


@to_async
def to_gather(sleep_time: int) -> int:
    print(f"start:{sleep_time}")
    time.sleep(sleep_time)
    print(f"finish:{sleep_time}")
    return sleep_time


async def main():
    res = await asyncio.gather(*(to_gather(i) for i in [2, 5, 3, 4, 5, 2, 2]))
    return res

if __name__ == "__main__":
    res = asyncio.run(main())
    print(res)
