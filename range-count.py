
import random
import time
import timeit

# Functions:

def linearScan(a, x):
	count = 0
	for n in a:
		if n == x:
			count += 1
	return count

def doubleBinary(a, x):
	firstOccurance = getStartIndex(a, x, 0, len(a) - 1)
	if firstOccurance == -1:
		return 0
	lastOccurance = getEndIndex(a, x, 0, len(a) - 1)
	return lastOccurance - firstOccurance + 1

def getStartIndex(a, x, low, high):
	if high >= low: 
		mid = (high + low) // 2
		if a[mid] == x:
			if mid == low: 
				return low
			elif a[mid-1] != x:
				return mid
			return getStartIndex(a, x, low, mid - 1)
		elif a[mid] > x:
			return getStartIndex(a, x, low, mid - 1) 
		else:
			return getStartIndex(a, x, mid + 1, high) 
	else:
		return -1

def getEndIndex(a, x, low, high):
	if high >= low: 
		mid = (high + low) // 2
		if a[mid] == x:
			if mid == high: 
				return high
			elif a[mid+1] != x:
				return mid
			return getEndIndex(a, x, mid + 1, high)
		elif a[mid] > x:
			return getEndIndex(a, x, low, mid - 1) 
		else:
			return getEndIndex(a, x, mid + 1, high) 
	else:
		return -1

# Benchmarking

def getSortedRandomArray(size):
	a = []
	for n in range(size):
		a.append(random.randint(0, 10))
	a.sort()
	return a

def getLinearPerformance(a, x):
	t0 = time.time()
	linearScan(a, x)
	return time.time() - t0

def getBinaryPerformance(a, x):
	t0 = time.time()
	doubleBinary(a, x)
	return time.time() - t0

size = 1
for i in range(7):
	size *= 10
	a = getSortedRandomArray(size)
	x = random.randint(0, 10)
	linearPerformance = getLinearPerformance(a, x)
	binaryPerformance = getBinaryPerformance(a, x)
	print(linearPerformance)
	print(binaryPerformance)
	print("---------------------")

