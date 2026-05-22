from typing import List, Dict


def generate_prime_sequence(total_required: int) -> List[int]:
    """
    Generate the first N prime numbers using a dictionary-based incremental sieve.

    This algorithm:
    - Avoids building a large array (unlike the classic sieve)
    - Tracks only composite numbers dynamically
    - Associates each composite with the prime that generated it
    - Moves composites forward as needed

    Args:
        total_required (int): Number of prime numbers to generate

    Returns:
        List[int]: A list containing the first N prime numbers
    """

    # Edge case: if no primes are requested, return empty list
    if total_required < 1:
        return []

    # Dictionary to track composite numbers:
    # key   → composite number
    # value → step size (the prime factor responsible for generating this composite)
    composite_tracker: Dict[int, int] = {}

    # List to store discovered prime numbers
    prime_collection: List[int] = []

    # Start checking from the first prime candidate
    candidate_value = 2

    # Continue until we collect the required number of primes
    while len(prime_collection) < total_required:

        # If the candidate is NOT in the tracker,
        # it means no smaller prime marked it → it's a prime
        if candidate_value not in composite_tracker:
            prime_collection.append(candidate_value)

            # Mark the first composite number for this prime
            # Start from p^2 (important optimization)
            composite_tracker[candidate_value * candidate_value] = candidate_value

        else:
            # Candidate is composite
            # Retrieve the step size (the prime that generated it)
            step_value = composite_tracker.pop(candidate_value)

            # Move this composite forward to the next multiple
            next_composite = candidate_value + step_value

            # Handle collisions:
            # If another prime already scheduled this number,
            # keep moving forward until we find a free slot
            while next_composite in composite_tracker:
                next_composite += step_value

            # Register the next composite in the tracker
            composite_tracker[next_composite] = step_value

        # Move to the next number
        candidate_value += 1

    return prime_collection


def main() -> None:
    """
    Entry point of the program.
    Demonstrates how to use the prime generator.
    """

    # Define how many primes to generate
    target_prime_count = 1000

    # Generate the prime numbers
    prime_numbers = generate_prime_sequence(target_prime_count)

    # Display summary information
    print(f"Total primes generated: {len(prime_numbers)}")
    print(f"First 10 primes: {prime_numbers[:10]}")
    print(f"Last prime ({target_prime_count}th): {prime_numbers[-1]}")

    # Optional: print all primes (uncomment if needed)
    # for prime_value in prime_numbers:
    #     print(prime_value)


# Standard Python entry point
if __name__ == "__main__":
    main()