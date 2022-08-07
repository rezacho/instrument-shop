from abc import ABC, abstractmethod
from config import instruments_list
import itertools


class Instrument(ABC):
    id_generator = itertools.count()

    def __init__(self, manufacture, price, *args, **kwargs):
        self.unique_id = next(self.id_generator)
        self.manufacture = manufacture
        self.price = price

    @staticmethod
    @abstractmethod
    def show_all_instruments():
        pass

    @staticmethod
    def search_instrument(instrument_id):
        for item in instruments_list:
            if instrument_id == item.unique_id:
                return item

    @abstractmethod
    def __str__(self):
        pass


class Guitar(Instrument):
    def __init__(self, string_count, string_type, wood_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.string_count = string_count
        self.string_type = string_type
        self.wood_type = wood_type

    @staticmethod
    def show_all_instruments():
        guitars = []
        for item in instruments_list:
            if isinstance(item, Guitar):
                guitars.append(item)
        return guitars

    def __str__(self):
        return f'- Id: {self.unique_id}\n- Brand: {self.manufacture}\n- Price: {self.price}$\n' \
               f'- String count: {self.string_count}\n- String type: {self.string_type}\n' \
               f'- Wood type: {self.wood_type}\n{"-"*30}'
