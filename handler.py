import os
from sys import platform
from models import *
from config import instrument_types, instruments_list


def clear_screen():
    if platform in ("linux", "linux2", "darwin"):
        return os.system('clear')
    elif platform == "win32":
        return os.system('cls')


class Run:
    chosen_instrument = None
    user_choice = None
    obj = None

    @staticmethod
    def ask_for_menu():
        user_choice = input('Press M for main menu: ').upper()
        if user_choice == 'M':
            clear_screen()
            Run().main_menu()
        exit()

    def chose_instrument(self):
        for instrument in instrument_types:
            print(f'{instrument_types.index(instrument)}. {instrument}')
        user_choice = input("Please choose your instrument type: ")
        self.chosen_instrument = instrument_types[int(user_choice)]
        clear_screen()
        return self.chosen_instrument

    def main_menu(self):
        print("*** Welcome To Instrument Shop ***")
        print("Main Menu:\n"
              "1. Add new instrument\n"
              "2. Show all instruments\n"
              "3. Find an instrument\n"
              )
        self.user_choice = input("Please Enter Your Choice: ")
        clear_screen()

        if self.user_choice == '1':
            self.chose_instrument()
            clear_screen()
            if self.chosen_instrument == "Guitar":
                self.obj = Guitar(manufacture=input("Manufacture: "),
                                  price=input("Price: "),
                                  string_count=input("String count: "),
                                  string_type=input("String type: "),
                                  wood_type=input("Wood type: "))
            instruments_list.append(self.obj)
            print(f"Instrument created successfully... ID: {self.obj.unique_id}")
            self.ask_for_menu()

        elif self.user_choice == '2':
            self.chose_instrument()
            if self.chosen_instrument == "Guitar":
                for guitar in Guitar.show_all_instruments():
                    print(guitar)
            self.ask_for_menu()

        elif self.user_choice == '3':
            self.user_choice = int(input('Enter instrument id: '))
            print(Instrument.search_instrument(self.user_choice))
            self.ask_for_menu()
