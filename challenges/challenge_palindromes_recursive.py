def is_palindrome_recursive(
    word: str, low_index: int, high_index: int
) -> bool:
    is_letter_equal = bool(word)
    if low_index <= high_index:
        is_letter_equal = word[low_index] == word[high_index]
        if is_letter_equal:
            return is_palindrome_recursive(word, low_index+1, high_index-1)
    return is_letter_equal
