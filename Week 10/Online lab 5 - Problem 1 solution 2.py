
# Place all function definitions required for Problem 1 in this cell.

import matplotlib.pyplot as mpl
import math
import statistics

def scherrer(b, deg):
    """scherrer function takes in `b` and `deg`
    and applies the Scherrer Equation.
    """
    return (0.9)*(0.07107)/b/math.cos(deg*math.pi/180)

def findBeta(angles, intensties, peakIndex):
    """findBeta funtion finds the beta value of each
    provided `peakIndex` using the given data.
    """
    
    # calculate the intensity of this peak's beta
    betaIntensity = intensties[peakIndex]/2
    
#     print(betaIntensity)
    
    # chop and orient two lists for each side of the peak
    # with index 0 as the peak
    leftCurve = intensties[:peakIndex+1]
    leftCurve.reverse()
    rightCurve = intensties[peakIndex:]
    
#     print(rightCurve)

    # Initialize left and right beta values as empty
    leftValue = None
    rightValue = None
    
    # while loop find value with smallest delta will end
    # once both `leftValue` and `rightValue` have a value
    prevLeftDelta = float("inf")
    prevRightDelta = float("inf")
    i = 0
    while not (leftValue and rightValue):
        leftDelta = abs(betaIntensity - leftCurve[i])
        rightDelta = abs(betaIntensity - rightCurve[i])
        
#         print(rightDelta)
        
        # once delta increaces from the previous,
        # the previous angle value is closest
        if not leftValue and prevLeftDelta < leftDelta:
            leftValue = angles[peakIndex - (i - 1)]
        if not rightValue and prevRightDelta < rightDelta:
            rightValue = angles[peakIndex + (i - 1)]
                    
        i += 1
        prevLeftDelta = leftDelta
        prevRightDelta = rightDelta
        
    return rightValue-leftValue
    
    
def getData(path):
    """getData function intakes `path` to stored 
    data and provides a list of `angles`,
    `intensities`, and `peakIndexes`.
    """
    
    # initialize lists
    angles = []
    intensties = []
    peakIndexes = []
    i = 0
    
    # open file and loop through each line
    file = open(path, "r")
    for line in file:
        values = line.split()
        angles.append(float(values[0]))
        
        # if value has '*', its a peak, remember the index
        # and strip the '*'' out
        if line.find('*') > -1:
            peakIndexes.append(i)
            intensties.append(float(values[1].strip('*')))
        else:
            intensties.append(float(values[1]))
                       
        i += 1
        
    return angles, intensties, peakIndexes
        
def showGraph(xAxis, yAxis, size):
    """showGraph function displays a graph of the
    given data.
    """
    
    # do graph stuff
    fig, ax = mpl.subplots()
    ax.set_xlabel('θ2 (deg.)')
    ax.set_ylabel('Intensity (a.u.)')
    ax.set_title("Nanoparticle Size Estimate: " + str(size) + " nm")
    ax.plot(xAxis, yAxis)
    
def XRD_Analysis(file):
    
    # get data
    angles, intensties, peakIndexes = getData(file)

    # collect particle sizes of each peak and average
    sizes = set()
    for n in peakIndexes:
        beta = findBeta(angles, intensties, n)
        sizes.add(scherrer(beta, angles[n]))
        
    size = statistics.mean(sizes)

    # show graph
    showGraph(angles, intensties, size)
    
    
    # return average size
    return size
    