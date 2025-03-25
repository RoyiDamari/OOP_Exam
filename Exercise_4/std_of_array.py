from handler import Handler
from typing import override
import statistics


class StdOfArray(Handler):
    """
    Asks if the user wants to calculate the standard deviation.
    If yes and there are at least 2 elements, it is calculated and stored.
    """

    @override
    def handle(self, number_array):
        while True:
            std_choice = input("Calculate standard deviation? (yes/no): ").strip().lower()
            if std_choice not in ["yes", "no"]:
                print("Invalid choice you mast enter (yes/no)")
                continue
            else:
                break

        if std_choice == "yes":
            if len(number_array.numbers) > 1:
                calculated_std = statistics.stdev(number_array.numbers)
                number_array.std_deviation = calculated_std
                print(f"Standard deviation: {number_array.std_deviation}")
            else:
                print("Cannot calculate standard deviation with less than 2 numbers")

        if self.next:
            self.next.handle(number_array)
