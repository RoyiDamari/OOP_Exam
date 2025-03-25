from number_array import NumberArray
from sort_the_array import SortTheArray
from multiply_the_array import MultiplyTheArray
from average_of_array import AverageOfArray
from std_of_array import StdOfArray


def main():
    # Create the numbers array
    while True:
        try:
            size = int(input("Enter the size of the array: "))
            break
        except ValueError:
            print("Invalid input. Please type a valid integer.")

    number_array = NumberArray(size)

    print(f"Original array: {number_array.numbers}")

    # Create handler instances
    sort_the_array = SortTheArray()
    multiply_the_array = MultiplyTheArray()
    average_of_array = AverageOfArray()
    st_dev_of_array = StdOfArray()
    chain_root = sort_the_array

    # link them in a chain
    sort_the_array.next = multiply_the_array
    multiply_the_array.next = average_of_array
    average_of_array.next = st_dev_of_array
    st_dev_of_array.next = None

    # start the chain
    chain_root.handle(number_array)

    # Print final array
    print(f"Final array: {number_array.numbers}")

    # Display stored statistics
    print("\nStored Statistics:")
    if number_array.average is not None:
        print(f"Average: {number_array.average}")
    if number_array.std_deviation is not None:
        print(f"Standard Deviation: {number_array.std_deviation}")


if __name__ == "__main__":
    main()
