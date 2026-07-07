# Week 01 — Big-O Exercises


# O(1) — Constant Time
def get_first(items):
    return items[0]


# O(n) — Linear Time
def print_items(items):
    for item in items:
        print(item)


# O(n) — Two separate loops are still linear
def print_items_twice(items):
    for item in items:
        print(item)

    for item in items:
        print(item)


# O(n²) — Quadratic Time
def print_pairs(items):
    for a in items:
        for b in items:
            print(a, b)


# O(log n) — Logarithmic Time
def halve_until_one(n):
    while n > 1:
        print(n)
        n = n // 2


# O(n log n) — Linear work repeated over logarithmic levels
def n_log_n_example(items):
    n = len(items)

    while n > 1:
        for item in items:
            print(item)

        n = n // 2


# Small manual tests
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    print("O(1):")
    print(get_first(numbers))

    print("\nO(n):")
    print_items(numbers)

    print("\nO(n) with two separate loops:")
    print_items_twice(numbers)

    print("\nO(n²):")
    print_pairs(numbers)

    print("\nO(log n):")
    halve_until_one(32)

    print("\nO(n log n):")
    n_log_n_example(numbers)