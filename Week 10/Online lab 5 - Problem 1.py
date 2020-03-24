
import matplotlib.pyplot as plt
import numpy as np
import math

#XRD_example1.txt
#XRD_example2.txt

KCONST = 0.9

WAVELENGTH = 0.07107 #defining constants

def Convert(file):

    filelines = file.readlines() #file handling

    degrees = []
    intensity = []

    peakDegrees = []
    peakIntensity = []

    for i in range(len(filelines)): #File handling - converting data into 4 lists

        line = filelines[i].split()

        currentdegrees = line[0]
        currentintensity = line[1]

        if currentintensity.find("*") > 0: #finding peak values and adding them to the peak lists

            stringfixed = currentintensity.replace("*","") #taking out the start for graphing and calculations

            peakDegrees.append(float(line[0]))
            peakIntensity.append(float(stringfixed))

            degrees.append(float(line[0]))
            intensity.append(float(stringfixed))

        else:

            degrees.append(float(line[0]))
            intensity.append(float(line[1]))

    return degrees,intensity,peakDegrees,peakIntensity

def Plottingthis(degrees,intensity):

    plt.plot() #plotting the data

    plt.plot(degrees,intensity)
    
    plt.xlabel("2θ (deg)") #formatting axis
    plt.ylabel("Intesnity (a.u.)")
    plt.title("XRD plot") 

    plt.show()

    return 1

def CalculateT(degrees,intensity,peakDegrees,peakIntensity):

    Bvalue = 0
    Bvalues = []

    TvalueAvg = 0
    Tvalues = []

    startiter = []

    for i in range(len(intensity)):
        for a in range(len(peakIntensity)):
            if degrees[i] == peakDegrees[a]-0.5:
                startiter.append(i) #Selecting the position to start the loop
    
    for i in range(len(peakIntensity)): #Calculating the B value for each peak

        halfMaxInt = peakIntensity[i]/2

        Bvalues.append(CalculateB(halfMaxInt,degrees,intensity, startiter[i]))

        BvalueRad = math.radians(Bvalues[i])

        Tvalues.append((WAVELENGTH*KCONST)/(BvalueRad*math.cos(math.radians(peakDegrees[i]))))

    avg = AverageT(Tvalues)

    return avg

def AverageT(Tvalues):

    TvalueAvg = sum(Tvalues)/len(Tvalues) #avaraging the values

    return TvalueAvg

def CalculateB(halfMaxInt,degrees,intensity, startpoint):

    Bmin = []
    Bmax = []

    for i in range(startpoint,len(degrees)): #finding the values cloeset to the desired half intensity

        if intensity[i] < halfMaxInt:

            d1 = intensity[i]

            d2 = intensity[i+1]

            if d2 > halfMaxInt:
                pass
        
        if intensity[i] > halfMaxInt:

            b1 = intensity[i]

            b2 = intensity[i+1]

            if b2 < halfMaxInt:
                break
    
    c1 = abs(halfMaxInt - b1)
    c2 = abs(halfMaxInt - b2) 

    a1 = abs(halfMaxInt - d1)
    a2 = abs(halfMaxInt - d2)

    if c1 > c2:
        Bmax.append(b2)
    else:
        Bmax.append(b1)

    if a1 > a2:
        Bmin.append(d2)
    else:
        Bmin.append(d1) #finding the closest intensity values to the desired value

    BminDegrees = 0 #converting those intensity values into degrees because i didnt read ahead
    BmaxDegrees = 0

    for i in range(startpoint,len(degrees)):
        if intensity[i] == Bmin[0]:
            BminDegrees = degrees[i]

        if intensity[i] == Bmax[0]:
            BmaxDegrees = degrees[i]

    Bvalue = abs(BmaxDegrees - BminDegrees) #determining the B value for given half intensity

    return Bvalue

def XDR_analysis(file): #Main, calls everthing

    data = open(file,'r')

    degrees,intensity,peakDegrees,peakIntensity = Convert(data) #Converts raw data into two lists

    Tvalue = CalculateT(degrees,intensity,peakDegrees,peakIntensity) #Calculating the T avg value

    Plottingthis(degrees,intensity) #Plotting the points

    print("T Value avg:" + str(Tvalue)) #Printing 

    return Tvalue

XDR_analysis("XRD_example1.txt")