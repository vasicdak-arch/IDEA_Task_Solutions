def generate_fizzbuzz_sequence(upper_limit: int) -> None:
    """
    Print the FizzBuzz sequence from 1 up to the given upper limit.

    Rules:
    - If a number is divisible by both 3 and 5 → print "FizzBuzz"
    - If divisible only by 3 → print "Fizz"
    - If divisible only by 5 → print "Buzz"
    - Otherwise → print the number itself

    Args:
        upper_limit (int): The maximum number in the sequence (inclusive)
    """

    # Iterate through numbers starting from 1 up to the upper limit
    for current_number in range(1, upper_limit + 1):

        # Check divisibility by both 3 and 5 first
        # (15 is the least common multiple of 3 and 5)
        if current_number % 15 == 0:
            print("FizzBuzz")

        # Check if divisible by 3
        elif current_number % 3 == 0:
            print("Fizz")

        # Check if divisible by 5
        elif current_number % 5 == 0:
            print("Buzz")

        # If none of the conditions match, print the number
        else:
            print(current_number)


def main() -> None:
    """
    Entry point of the program.
    """

    # Define how many results you want
    result_limit = 100

    # Generate and print the FizzBuzz sequence
    generate_fizzbuzz_sequence(result_limit)


# Standard Python entry point check
if __name__ == "__main__":
    main()