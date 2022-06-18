import numpy
import os

file_location = os.path.join('data','distance_data_headers.csv')
#testung purposes
#print(file_location)
#can use the help function if you do not know how to integrate a function
#help(numpy.genfromtxt)
#delimeter -> symbol that needs to be removed from data
distances = numpy.genfromtxt(fname = file_location, delimiter = ',', dtype ='unicode')

#testing purposes
#print(distances[0])

headers = distances[0]
data = distances[1:]

#testing purposes
#print(data)

#convert values from headers to type float
data = data.astype(float)
#testing purposes
#print(data)

#array_name[row, col]
#printing cells in array
print(data[0,1])

#printing data start from row 0-10 and col 0-3
small_data = data[0:10, 0:3]
print(small_data)

#loop through data while x is between 1 and the num of columns
for x in range(1,num_columns):
    #increment the the olumns
    data_column = data[:,x]
    #find the average of data in columns
    average = numpy.mean(data_column)
    print(F'{average}')
