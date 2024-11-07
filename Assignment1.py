#Import the required packages
from matplotlib import pyplot
import numpy

def read_data(inputfile):
    x=[]
    y=[]
    # open the data file
    with open(inputfile,"r") as myfile:
    # Read all lines
        lines=myfile.readlines()
    for line in lines:
        elements = line.split()
        x.append(float(elements[0]))
        ydata = [float(i) for i in elements[1:]]
        y.append(ydata)


    pyplot.plot(x, y)
    # Labeling the axes and title
    pyplot.ylabel("y")
    pyplot.xlabel("x")
    pyplot.title("Task1")
    # Send the plot to the screen
    pyplot.grid(linestyle="-")
    pyplot.show ()

    return
if __name__ =='__main__' :
    read_data('data/plenty.data')










