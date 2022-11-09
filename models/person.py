from unicodedata import name


class Person:
    """Person Object"""
    
    ORDER = (LASTNAME, FIRSTNAME, OTHER_NAMES) = (1, 2, 3)
    
    last_name: str
    first_name: str
    other_names: str = ""
    birth_date: str
    birth_gender: str
    
    
    def __init__(self, last_name, first_name, other_names = "", \
        name_order = ORDER) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.other_names = other_names
        if set(self.ORDER) == set(name_order):
            self.ORDER = name_order
        else:
            raise ValueError()
        

    def get_name_attrs(self, order: tuple[int]):
        for _ in order

    def full_name(self, order: tuple[int] = ORDER):
        return "{}{}{}".format()
