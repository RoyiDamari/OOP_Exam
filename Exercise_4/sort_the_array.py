from handler import Handler
from typing import override


class SortTheArray(Handler):
    """
    Asks if the user wants to sort the numbers. If yes, it sorts
    the array in ascending order, then passes the request on.
    """

    @override
    def handle(self, number_array):
        while True:
            sort_choice = input("Sort the array? (yes/no): ").strip().lower()
            if sort_choice not in ["yes", "no"]:
                print("Invalid choice you mast enter (yes/no)")
                continue
            else:
                break

        if sort_choice == "yes":
            sorted_numbers = sorted(number_array.numbers)
            number_array.numbers = sorted_numbers
            print(f"Sorted array: {number_array.numbers}")

        if self.next:
            self.next.handle(number_array)
