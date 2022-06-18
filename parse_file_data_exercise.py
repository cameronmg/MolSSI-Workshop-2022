import os
import numpy

def calculate_distance(coords1, coords2):
    xdist = coords1[0] - coords2[0]
    ydist = coords1[1] - coords2[1]
    zdist = coords1[2] - coords2[2]
    
    distance = numpy.sqrt(xdist**2+ydist**2+zdist**2)
    return distance  

def bond_check(distance, min_value = 0, max_value = 1.5):
    """
This function takes in user input and checks the distance if it is a bond.
    """
    if distance < max_value and distance > min_value:
        return True
    else:
        return False  
    
#write a new function to open and process a xyz file
#return list of symbols and coordinates
def open_file(path):
    """
    This function proccess a file and returns the data in the file as an array. 
    Enter the file name and the data will be returned.
    """
    xyz_file_path = os.path.join(path)
    xyz_file = numpy.genfromtxt(fname = file_location, dtype ='unicode', skip_header = 2)
    
    symbols = xyz_file[:,0]
    #store cordiantes starts from column 1 to the end of matrix in list coorinates
    coordinates = xyz_file[:,1:]
    #convert coordinates to type float
    coordinates = coordinates.astype(float)
    
    return symbols,coordinates

file_location = input('Enter the file path to the .xyz file: ')
symbols, coordinates = open_file(file_location)
num_atoms = len(symbols)

for num1 in range(0, num_atoms):
    for num2 in range(0, num_atoms):
        if num1 < num2:
            distance = calculate_distance(coordinates[num1],coordinates[num2])
            if bond_check(distance) is True:
                print(F'{symbols[num1]} to {symbols[num2]} : {distance:.3f}')
