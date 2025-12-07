def is_prime(n: int) -> bool:
    return True


test_values = {
    "negative": -5,
    "zero": 0,
    "one": 1,
    "small_prime_2": 2,
    "small_prime_3": 3,
    "small_prime_5": 5,
    "small_composite_4": 4,
    "small_composite_6": 6,
    "small_composite_9": 9,
    "large_prime_97": 97,
    "large_composite_100": 100,
}

for label, value in test_values.items():
    print(label, value, is_prime(value))
