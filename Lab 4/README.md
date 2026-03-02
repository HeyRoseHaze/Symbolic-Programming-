# Lab 4

## Task 1

Write a function that takes a temperature value in Kelvin and returns the value expressed in degrees Celsius:

**TC = TK − 272.15**

If a negative value is provided, the function should return None. Test its functionality.

## Task 2 

Write a function that returns the sum of the first **N** terms of the Maclaurin series expansion of **exp(x)**.

The values **x** and **N** should be function arguments.  
Set the default value of **N** to 50.

## Task 3

The spectral series of hydrogen are described by the following formula (https://pl.wikipedia.org/wiki/Serie_widmowe_wodoru):

$$\frac{1}{\lambda} = R_\infty \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right)$$

where:

- **λ** – wavelength of the photon corresponding to the transition from shell *n₂* to shell *n₁*  
- **n₁, n₂** – orbital numbers between which the transition occurs (*n₁ < n₂*)  
- **R∞ ≈ 0.0109737 nm⁻¹** – Rydberg constant  

Write a program that prints the wavelengths of several hydrogen spectral series, for example in the following form:
```text
Spectral lines for n1 = 1:
n2 = 2 : lambda = 122 nm
n2 = 3 : lambda = 103 nm
n2 = 4 : lambda = 97 nm

Spectral lines for n1 = 2:
n2 = 3 : lambda = 656 nm
n2 = 4 : lambda = 486 nm
n2 = 5 : lambda = 434 nm
```

## Taks 4

Write two functions that calculate the factorial of a number given as an argument:

- one implemented **iteratively**
- one implemented **recursively**

Test both functions to verify that they work correctly.
