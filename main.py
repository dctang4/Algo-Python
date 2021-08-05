# Write a function that returns the sum of two numbers.

def add(param1, param2):
  return param1 + param2

print(add(2,5))

###########################################

# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

def centuryFromYear(year):
  return (year+99)//100

print(centuryFromYear(1809))

###########################################

# Given the string, check if it is a palindrome.

def checkPalindrome(inputString):
  return inputString == inputString[::-1]

print(checkPalindrome('noon'))

###########################################

# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

def adjacentElementsProduct(inputArray):
  return max([inputArray[i]*inputArray[i+1] for i in range(len(inputArray)-1)])

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))

###########################################

# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. 

def shapeArea(n):
  return n**2 + (n-1)**2

print(shapeArea(5))

###########################################

# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

def makeArrayConsecutive2(statues):
  return max(statues) - min(statues) - len(statues) + 1

print(makeArrayConsecutive2([6, 2, 3, 8]))

###########################################

# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

def almostIncreasingSequence(sequence):
  count = 0
  i = 0
  while i < len(sequence) -1:
    if sequence[i] >= sequence[i+1]:
      count += 1
      if i > 0 and i < len(sequence)-2 and sequence[i-1] >= sequence[i+1] and sequence[i] >= sequence[i+2]:
        return False
      if count > 1:
        return False
                
    i += 1
                
  return True

print(almostIncreasingSequence([10, 1, 2, 3, 4, 5]))

###########################################

# After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

def matrixElementsSum(matrix):
  count = 0
  for j in range(len(matrix[0])):
    for i in range(len(matrix)):
      if matrix[i][j] == 0:
        break
      else:
        count += matrix[i][j]
  return count

print(matrixElementsSum([ [0, 1, 1, 2], 
                          [0, 5, 0, 0], 
                          [2, 0, 3, 3] ]))