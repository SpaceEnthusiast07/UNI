#############################################################
## This program contains many different sorting algorithms ##
## and compares their sorting times on the same array      ##
#############################################################

import numpy as np
import time, threading

# Sorting animation
def animate(message, iterations):
	for i in range(iterations):
		print(f"{message}    ", end="\r")
		time.sleep(0.2)
		print(f"{message} .  ", end="\r")
		time.sleep(0.2)
		print(f"{message} .. ", end="\r")
		time.sleep(0.2)
		print(f"{message} ...", end="\r")
		time.sleep(0.2)


# Bubble sort
def bubbleSort(array):
	swapped = True

	start = time.time()
	
	while swapped:
		swapped = False
		for i in range(len(array)-1):
			if (array[i] > array[i+1]):
				temp = array[i+1]
				array[i+1] = array[i]
				array[i] = temp
				swapped = True
	
	end = time.time()
	results["bubble"] = end - start


# Selection sort
def selectionSort(array):
	unsortedSection = 0
	start = time.time()

	while unsortedSection < len(array):
		smallestValue = 1e100
		smallestValueIndex = 0

		for i in range(unsortedSection, len(array)):
			if (array[i] < smallestValue):
				smallestValue = array[i]
				smallestValueIndex = i
		
		array[smallestValueIndex] = array[unsortedSection]
		array[unsortedSection] = smallestValue
		unsortedSection += 1
	
	end = time.time()
	results["selection"] = end - start


# Insertion sort
def insertionSort(array):
	start = time.time()

	for i in range(1, len(array)):
		key = array[i]
		j = i-1

		while(j >= 0 and key < array[j]):
			array[j+1] = array[j]
			j -= 1
		
		array[j+1] = key
	
	end = time.time()
	results["insertion"] = end - start


# Merge sort
def mergeSort(array):
	if(len(array) == 1):
		return array
	
	middle = (0 + len(array)) // 2
	leftHalf = mergeSort(array[0,middle])
	rightHalf = mergeSort(array[middle+1, len(array)-1])

def combineArrays(array1, array2):
	combinedArray = []

	for i in range(len(array1)):
		for j in range(len(array2)):
			


# Generate an array of 1000 random integers from 1 to 10000
size = 10000
maxInt = 100000
unsortedArray = np.random.randint(maxInt, size=size) + 1
results = {}

# Display the information about the competition
print("\n === Sorting Algorithm Competition ===")
print(f"Info:\n   - Each algorithm is sorting the same random array\n   - The array has {size} elements, between 1 and {maxInt}\n")

# Logic Behind next section
#  - I use threads so that I can display a sorting animation 
#    whilst the sorting function is actively sorting
#  - The "while(t.is_alive())" loop ensures the animation keeps rendering
#    while the algorithm is still sorting and not before or after it has 
#    finished sorting

# Run the bubble sort func on another thead
#t = threading.Thread(target=bubbleSort, args=(unsortedArray,))
#t.start()
#while(t.is_alive()):
#	animate("Sorting", 1)
#t.join()
#print(f"Bubble sort: {results['bubble']: .4f} seconds")

# Run the selection sort func on another thead
t = threading.Thread(target=selectionSort, args=(unsortedArray.copy(),))
t.start()
while(t.is_alive()):
	animate("Sorting", 1)
t.join()
print(f"Selection sort: {results['selection']: .4f} seconds")

# Run the insertion sort func on another thead
t = threading.Thread(target=insertionSort, args=(unsortedArray.copy(),))
t.start()
while(t.is_alive()):
	animate("Sorting", 1)
t.join()
print(f"Insertion sort: {results['insertion']: .4f} seconds")