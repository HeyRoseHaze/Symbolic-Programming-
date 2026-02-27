
def wavelength(n):
    n2 = [n + 1, n + 2, n + 3]

    for n2 in n2:
        wavelenght = (rydberg * (1 / (n ** 2) - 1 / (n2 ** 2))) ** -1
        print(f'The wavelenght for n1 = {n} is equal to:')
        print(f'n = {n2} , lambda = {wavelenght:.3f} [nm]')


rydberg = 0.0109747 

wavelength(1)