# Lab 3

## Task 1

Write a program that prints the first N natural numbers in ascending and descending order in separate columns:
0 5
1 4
2 3
3 2
4 1
5 0

## Task 2 

Write a program that calculates the sum of the first $N$ terms of the Maclaurin series expansion for the function $e^x$:

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$$

for an $x$ provided by the user. Calculate the approximation using the series formula. Compare the result with the actual value calculated by the `exp` function from the `math` library.

## Task 3

Perfect numbers are those that are the sum of their proper divisors. Write a program that checks whether a given natural number is a perfect number.

## Taks 4

Write a program that asks the user to enter a natural number, and then prints the number of digits in the entered value, as well as the sum of its digits. For simplicity, assume that the entered number is valid.

## Task 5

Write a program that performs the following steps:

1.  Creates an empty list and fills it with five random numbers from an arbitrary range, e.g., $[-1, 1]$.
2.  Prints all elements of the list sequentially along with their indices in the following format:
    ```text
    list[0]: 0.1
    list[1]: -0.92
    etc.
    ```
3.  Prints the length of the list (the number of its elements).
4.  Finds and prints the largest element of the list and its index.
