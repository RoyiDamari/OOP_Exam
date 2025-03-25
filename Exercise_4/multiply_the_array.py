from handler import Handler
from typing import override


class MultiplyTheArray(Handler):
    """
    Asks if the user wants to multiply each number by a factor.
    If yes, performs the multiplication and then passes on.
    """

    @override
    def handle(self, number_array):
        while True:
            multiply_choice = input("Multiply array elements by a number? (yes/no): ").strip().lower()
            if multiply_choice not in ["yes", "no"]:
                print("Invalid choice you mast enter (yes/no)")
                continue
            else:
                break

        if multiply_choice == "yes":

            while True:
                try:
                    factor = int(input("Enter the multiplication factor: "))
                    break
                except ValueError:
                    print("Invalid input. Please type a valid integer.")

            multiplied_numbers = [num * factor for num in number_array.numbers]
            number_array.numbers = multiplied_numbers
            print(f"Array after multiplication: {number_array.numbers}")

        if self.next:
            self.next.handle(number_array)
