from dataclasses import dataclass
from sys import getsizeof


@dataclass
class Data:
    asd: dict
    qwe: str
    zxc: int

data = Data(asd="", qwe="", zxc="")

data.asd
data.qwe
data.zxc


print(getsizeof(data))
print(getsizeof(data.__dict__))