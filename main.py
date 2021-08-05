def add(param1, param2):
  return param1 + param2

print(add(2,5))

###########################################

def centuryFromYear(year):
  return (year+99)//100

print(centuryFromYear(1809))

###########################################

def checkPalindrome(inputString):
  return inputString == inputString[::-1]

print(checkPalindrome('noon'))

###########################################

def adjacentElementsProduct(inputArray):
  return max([inputArray[i]*inputArray[i+1] for i in range(len(inputArray)-1)])

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))

###########################################

def shapeArea(n):
  return n**2 + (n-1)**2

print(shapeArea(5))

###########################################

def makeArrayConsecutive2(statues):
  return max(statues) - min(statues) - len(statues) + 1

print(makeArrayConsecutive2([6, 2, 3, 8]))

###########################################

