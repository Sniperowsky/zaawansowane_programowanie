import re

VOWELS = set("aeiouyąęó")


def is_palindrome(text: str) -> bool:
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def count_vowels(text: str) -> int:
    return sum(1 for ch in text.lower() if ch in VOWELS)


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("discount must be between 0 and 1")
    return float(price * (1 - discount))


def flatten_list(nested_list: list) -> list:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def word_frequencies(text: str) -> dict:
    freq = {}
    for word in re.findall(r"\w+", text.lower()):
        freq[word] = freq.get(word, 0) + 1
    return freq


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True