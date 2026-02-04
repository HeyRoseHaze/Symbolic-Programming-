

def is_even(number):
    return number % 2 == 0

def is_uneven(number):
    return number % 2 != 0

def main():
    numbers = []
    n = 0
    c_n = 1
    limit = 1_000_000

    while c_n < limit:
        numbers.append(c_n)
        c_n = ((4 * n + 2) / (n + 2)) * c_n
        n += 1

    even_numbers = sum(1 for num in numbers if is_even(num))
    uneven_numbers = sum(1 for num in numbers if is_uneven(num))

    print(f"Catalan_numbers: {numbers}")
    print(f"Number of evens: {even_numbers}")
    print(f"Number of odds: {uneven_numbers}")


if __name__ == "__main__":
    main()
