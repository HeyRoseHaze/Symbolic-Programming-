
def wavelength(n):
    print(f'\nThe wavelenght for n1 = {n} is equal to:')
    for n2 in range(n + 1, n + 4):
        wavelenght = (rydberg * (1 / (n ** 2) - 1 / (n2 ** 2))) ** -1
        print(f'n2 = {n2} , lambda = {wavelenght:.3f} [nm]')


rydberg = 0.0109747 

for n in range(1,5):
    wavelength(n)