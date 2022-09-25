import calendar

# known constants

class NamedDate():
    _current_index = 0
    _range: tuple[int] = (0, 0)
    _lang: str = "en"
    _names: dict[str, list] = {
        "en": [
            # [name1, abbr1], [name2, abbr2],
        ],
        "fr": [
            # [nom1, abr1], [nom2, abr2],
        ]
    }
    
    def __init__(self, entry: str|int, lang: str = "en") -> None:
        self._lang = lang
        if self.is_valid(entry):
            self._current_index = entry
        else:
            raise ("invalid month number entered: " + str(entry))

    def is_valid(self, entry: str|int) -> bool:
        if str(entry).isnumeric():
            return self.__validate_index(int(entry))
        if entry.isalpha():
            return self.__validate_name(entry)
        return False

    def __validate_index(self, index: int) -> int | bool:
        if self.__range[0] <= index <= self.__range[1]:
            return index
        return False

    def __validate_name(self, name: str) -> int | bool:
        for i in range(len(self._names[self._lang])):
            if name in self._names[self._lang][i]:
                return i + 1
        return False
    
    def get_index(self, name: str) -> int|bool:
        index = self.__validate_name(name)
        if index == False:
            return None
        return index

    def get_name(self, index: int) -> str:
        index: int|bool = self.__validate_index(index)
        if index == False:
            return None
        return self._names[self._lang][index-1][0]

    def get_abbreviation_by_index(self, index: int) -> str:
        index: int|bool = self.__validate_index(index)
        if index == False:
            return None
        return self._names[self._lang][index-1][1]


class Days(NamedDate):
    _range: tuple[int] = (1, 7)
    _lang: str = "en"
    _names: dict[str, list] = {
        "en": [
            ["Monday", "Mon"],
            ["Tuesday", "Tue"],
            ["Wednesday", "Wed"],
            ["Thursday", "Thur"],
            ["Friday", "Fri"],
            ["Saturday", "Sat"],
            ["Sunday", "Sun"],
        ]
    }
    
    def __init__(self, day: str|int, lang = "en") -> None:
        super().__init__(entry= day, language= lang)


class Months(NamedDate):

    _current_index: int = -1
    _range = (1, 12)
    _lang: str = "en"
    _names: dict[str, list] = {
        "en": [
            ["january", "jan"], ["february", "feb"], ["march", "mar"], ["april", "apr"],
            ["may", "may"], ["june", "jun"], ["july", "jul"], ["august", "aug"],
            ["september", "sept"], ["october", "oct"], ["november", "nov"], ["december", "dec"]
        ]
    }
    
    def __init__(self, month: str, lang = "en") -> None:
        super().__init__(entry=month, lang = lang)


def is_leap(year: int) -> bool:
    """Checks if enter year is a leap year

    Args:
        year (int): year in integer

    Returns:
        bool: Returns True for leap year and False otherwise
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def month_days(month: int, year: int = None) -> int:
    """Returns the number of days in a month

    Args:
        month (int): month index ie: 1: January; 2: February; ...

    Returns:
        int: The number of days in that month
    """
    if month == 2:
        return 28 + int(year is not None and is_leap(year))
    elif (0 < month < 8 and month % 2 == 1) or (8 <= month <= 12 and month % 2 == 0):
        return 31
    else:
        return 30
    
