from handler import Handler
from typing import override


class AverageOfArray(Handler):
    """
    Asks if the user wants to calculate the average of the numbers.
    If yes, calculates and stores the average, then passes on.
    """

    @override
    def handle(self, number_array):
        while True:
            average_choice = input("Calculate average? (yes/no): ").strip().lower()
            if average_choice not in ["yes", "no"]:
                print("Invalid choice you mast enter (yes/no)")
                continue
            else:
                break

        if average_choice == "yes":
            calculated_average = sum(number_array.numbers) / len(number_array.numbers)
            number_array.average = calculated_average
            print(f"Average of numbers: {number_array.average}")

        if self.next:
            self.next.handle(number_array)
