"""Executable that takes an integer as input and outputs its color using HexSieve data"""

def getFileDirectory(dataDir, number):

    pathNumber = str(number // 10**13) # truncate number to 10 trillion (file increment)

    #TODO: Check the number of digit needed in path
    return dataDir + '/' + pathNumber[0] + '/' + pathNumber[1:3] + '/' + pathNumber[3:5] + '/' + pathNumber[5:7] + '/' + pathNumber[7:9] + '.txt'

def getLineNumber(number):
    return (number // 10**11) % 100

def getFloorColor(dataDir, number):
    # use getFileDirectory to get file location
    # read file
    # use getLineNumber and return that line number's value

def searchNumber(floorColor, number):
    # call hexWrapper (need to import) with start color as floorColor and number as end
    # return result

# run this function when file is executed
def seek(dataDir, number):
    return searchNumber(getFloorColor(dataDir, number), number)
