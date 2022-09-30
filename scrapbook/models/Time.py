# the idea is to define Time according to periods 
# in such a way that their objects can be related
# to each other

class BaseTime():
    
    _name: str = None
    _range: tuple[int, int] = None
    _base: list[dict[str, tuple]] = None
    _head: list[dict[str, tuple]] = None
    
    def __init__(self, child = [], parent = []) -> None:
        self._base = child
        self._head = parent


class YearTime(BaseTime):
    
    _name: str = "year"
    _range: tuple[int, int] = None
    _base: list[dict[str, tuple]] = [
        {
            "month" : ""
        }
    ]

    def __init__(self, child=[], parent=[]) -> None:
        super().__init__(MonthTime, parent)


class MonthTime(BaseTime):
    
    _name: str = "month"
    _range: tuple[int, int] = (1, 12)
    
    def __init__(self) -> None:
        super().__init__()


class DayTime(BaseTime):
    
    _name: str = "day"
    _range: tuple[int, int] = (1, 30)
    
    def __init__(self) -> None:
        super().__init__()
