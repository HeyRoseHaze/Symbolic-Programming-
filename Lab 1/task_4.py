import math

coord_x = int(input('Enter x coordinate: '))
coord_y = int(input('Enter y coordinate: '))
coord_z = int(input('Enter z coordinate: '))

# Spherical Coordinate System

r = math.sqrt(coord_x ** 2 + coord_y ** 2 + coord_z ** 2)

phi = math.atan(coord_y/coord_x)

theta = math.asin(coord_z/r)

spherical_coordinates = [r, phi, theta]

print(f'\nThe spherical coordinates are:')
for coord in spherical_coordinates:
    print(coord)


# Cylindrical Coordinate System

p = math.sqrt(coord_x ** 2 + coord_y ** 2)

phi = math.atan(coord_y/coord_x)

z = coord_z

cylindrical_coordinates = [p, phi, z]

print(f'\nThe cylindrical coordinates are:')
for coord in cylindrical_coordinates:
    print(coord)