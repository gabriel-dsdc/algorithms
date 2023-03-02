def is_palindrome_iterative(word: str) -> bool:
    if not word:
        return False

    for i in range(1, len(word) + 1):
        if word[i - 1] != word[-i]:
            return False

    return True
