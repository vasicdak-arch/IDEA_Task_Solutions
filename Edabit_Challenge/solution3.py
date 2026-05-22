def execute_double_character_swap(
    input_text: str,
    primary_character: str,
    secondary_character: str
) -> str:
    """
    Swap all occurrences of two characters in a string.

    This implementation uses:
    - A mapping dictionary for constant-time lookups
    - A generator expression for efficient iteration
    - A clean fallback mechanism for unchanged characters

    Args:
        input_text (str): The original string
        primary_character (str): First character to swap
        secondary_character (str): Second character to swap

    Returns:
        str: Modified string with characters swapped
    """

    # Edge case: if both characters are the same, no swap needed
    if primary_character == secondary_character:
        return input_text

    # Create a swap mapping
    character_mapping = {
        primary_character: secondary_character,
        secondary_character: primary_character
    }

    # Build the result using a generator expression
    # For each character:
    # - If it's in the mapping → swap it
    # - Otherwise → keep it unchanged
    transformed_text = "".join(
        character_mapping.get(current_char, current_char)
        for current_char in input_text
    )

    return transformed_text


def main() -> None:
    """
    Example usage and simple test cases.
    """

    sample_text = "random string"
    first_char = "a"
    second_char = "o"

    result = execute_double_character_swap(
        sample_text,
        first_char,
        second_char
    )

    print(f"Original: {sample_text}")
    print(f"Swapped : {result}")


if __name__ == "__main__":
    main()