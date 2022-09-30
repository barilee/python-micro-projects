# base constants
hr_secs = 3600
day_secs = 86400
wk_secs = 604800
yr_mons = 12
wk_days = 7
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year_days = 365

(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEPT, OCT, NOV, DEC) = range(1,13)
(MON, TUE, WED, THUR, FRI, SAT, SUN) = range(1, 8)
wk_day_first = MON

class DateType:
    
    day, week, month, year = range(1,5)
    types = ("day", "week", "month", "year")

class InvalidDateTypeError(ValueError):
    def __init__(self, datetype: int, value: int, message: str = "") -> None:
        self.__date_value = value
        self.__date_type = DateType.types[datetype]
        self.__message = f" {message}".strip()
    def __str__(self) -> str:
        return "invalid {} number: {}.{}".format(self.__date_type, self.__date_value, self.__message)


class InvalidMonthError(InvalidDateTypeError):
    
    def __init__(self, month:int) -> None:
        super().__init__(DateType.month, month, "Number must be 1 - 12")


class InvalidYearError(ValueError):
    
    def __init__(self, year: int) -> None:
        super().__init__(DateType.year, year, "Number must not be zero (0)")


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
        self.set_current(entry)

    def is_valid(self, entry: str|int) -> bool:
        if str(entry).isnumeric():
            return self._validate_index(int(entry))
        if entry.isalpha():
            return self._validate_name(entry)
        return False

    def _validate_index(self, index: int) -> int | bool:
        if self._range[0] <= index <= self._range[1]:
            return index
        return False

    def _validate_name(self, name: str) -> int | bool:
        for i in range(len(self._names[self._lang])):
            if name.lower() in self._names[self._lang][i]:
                return i + 1
        return False

    def set_current(self, entry: str|int):
        entry = self.is_valid(entry)
        if entry != False:
            self._current_index = entry - 1
        else:
            raise Exception("invalid entry: " + str(entry))

    def get_details(self) -> list[str]:
        return self._names[self._lang][self._current_index]

    def get_index(self) -> int:
        return self._current_index + 1

    def get_name(self) -> str:
        return self.get_details()[0].capitalize()

    def get_abbreviation(self) -> str:
        return self.get_details()[1].capitalize()

    def get_index_by_name(self, name: str) -> int|bool:
        index = self._validate_name(name)
        return index | None 

    def get_name_by_index(self, index: int) -> str:
        index: int|bool = self._validate_index(index)
        if index == False:
            return None
        return self._names[self._lang][index-1][0]

    def get_abbreviation_by_index(self, index: int) -> str:
        index: int|bool = self._validate_index(index)
        if index == False:
            return None
        return self._names[self._lang][index-1][1]


class Days(NamedDate):
    _range: tuple[int] = (1, 7)
    _lang: str = "en"
    _names: dict[str, list] = {
        "en": [
            ["monday", "mon"],
            ["tuesday", "tue"],
            ["wednesday", "wed"],
            ["thursday", "thur"],
            ["friday", "fri"],
            ["saturday", "sat"],
            ["sunday", "sun"],
        ]
    }
    
    def __init__(self, day: str|int, lang = "en") -> None:
        super().__init__(entry= day, lang= lang)


class Months(NamedDate):

    _current_index: int = -1
    _range = (1, 13)
    _lang: str = "en"
    _names: dict[str, list] = {
        "en": [
            ["january", "jan"], ["february", "feb"], ["march", "mar"], ["april", "apr"],
            ["may", "may"], ["june", "jun"], ["july", "jul"], ["august", "aug"],
            ["september", "sept"], ["october", "oct"], ["november", "nov"], ["december", "dec"]
        ]
    }
    days = month_days 
    
    def __init__(self, month: str, lang = "en") -> None:
        super().__init__(entry=month, lang = lang)

    def num_days_by_end(self, month: int, year: int) -> int:
        return sum(self.days[:month]) + int(month >=2 and is_leap(year))


def is_leap(year: int) -> bool:
    """Checks if enter year is a leap year

    Args:
        year (int): year in integer

    Returns:
        bool: Returns True for leap year and False otherwise
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def num_leap_in(year: int, from_year: int = 0) -> int:
    """
    Calculates the number of leap years that will occur within the specified period.
    If {from_year} is passed, then the absolute number of leaps between {year} and {from_year} will be calculated, otherwise only the number of leaps in {year}

    Args:
        year (int): the period in years
        from_year (int, optional): the other period in years. Defaults to 0.

    Returns:
        int: Returns the number of leap years that will occur
    """
    if year == 0:
        return 0
    # leap year is 1 in 4 except in 100s (centuries) during which it is 1 in 400
    return abs((year//4 - year//100 + year//400) \
        - (from_year//4 - from_year//100 + from_year//400))

def num_days_until(day: int, from_day) -> int:
    return (wk_days - from_day + day) % wk_days 

def num_year_days(year: int):
    if year == 0:
        return year
    return year_days + int(is_leap(year))

def num_month_days(month: int, year: int = 0) -> int:
    """Returns the number of days in a month

    Args:
        month (int): month index ie: 1: January; 2: February; ...

    Returns:
        int: The number of days in that month
    """
    if month == 0:
        return 0
    return Months.days[month-1] + int(month ==2 and is_leap(year))

def num_wk_days_until(day: int, after: int) -> int:
    return (wk_days - after + day) % wk_days

def num_days_to_month(month: int, year: int) -> int:
    return ()

def num_days_by_date(day: int, month: int, year: int):
    return (year_days * (year - 1) + num_leap_in(year - 1)) \
        + Months.num_days_by_end(Months, month - 1, year) + day

def num_date_secs(day: int, month: int, year: int):
    return num_days_by_date(day, month, year) * day_secs

def month_first_day(month: int, year: int):
    # Jan 01/01/0001 is Saturday
    # Jan 03/01/0001 is Monday
    num_days_until(wk_day_first, )

    num_days_by_date(1, month, year)
    # subtract num of seconds before Monday
    pass


class BaseCalendar():
    
    root_first_day = SAT
    week_first_day = MON
    
    def month_first_day(self, month: int, year: int) -> int:
        # known fact: Jan 1st, 0001 is a Saturday
        # offset = num_wk_days_until(self.week_first_day, self.root_first_day)
        return (num_days_by_date(1, month, year) % 7 + 6 - self.root_first_day) % wk_days
