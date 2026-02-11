# Lab 2

## Task 1

Write a program that calculates the area and circumference of a circle with a radius provided by the user. Take the value of the constant π from the math library. 
The radius cannot be negative. If a negative number is entered, the program should display a message informing about the invalid value and perform no calculations.

## Task 2 

Write a program that asks for the coefficients of a quadratic equation $ax^2 + bx + c = 0$ and prints the solutions to the equation (or a message stating that there are no solutions).

## Task 3

Write a program that generates a random integer between 0 and 10 (using the randint function from the random library). The program should then ask the user to guess the number until they provide the correct value. 
Once the program works, extend it by adding information about the number of attempts it took to guess correctly, or by providing hints such as 'The number you entered is greater/smaller than the target number'.

## Taks 4

Catalan numbers (see [Wikipedia](https://en.wikipedia.org/wiki/Catalan_number)) form a sequence that can be expressed by the following recursive formula:

$$C_0 = 1$$
$$C_{n+1} = \frac{4n + 2}{n + 2} C_n$$

Write a program that prints all Catalan numbers smaller than one million and provides the count of **even** and **odd** numbers among them. 
