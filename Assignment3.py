import matplotlib.pyplot as plt
import numpy as np

#############################################################

def linear_search(arr, n, x):

	comparisons_count = 0

	for i in range(0, n):
		comparisons_count = comparisons_count + 1

		if (arr[i] == x):
			return i,comparisons_count

	return -1

#############################################################

def binary_search(arr, m, l, r):

    comparison_count = 0

    while l <= r:
        comparison_count = comparison_count + 1

        mid = l + (r - l)//2
        if arr[mid] == m:
            return mid, comparison_count
        elif arr[mid] < m:

            l = mid + 1
        else:

            r = mid - 1
    return -1


#############################################################

arr_100 = list(range(0,100))
arr_1000 = list(range(0,1000))
n_100 = len(arr_100)
n_1000 = len(arr_1000)

#############################################################


comparisons_number_100_L = 0

for num in arr_100:
	result,count = linear_search(arr_100, n_100, num)
	comparisons_number_100_L = comparisons_number_100_L + count
	#print(f"For number {num} Element index location is {result} and number of comparisons {count}")

average_number_of_comparisons_100_L = comparisons_number_100_L / n_100

comparisons_number_1000_L = 0

for num in arr_1000:
	result,count = linear_search(arr_1000, n_1000, num)
	comparisons_number_1000_L = comparisons_number_1000_L + count
	#print(f"For number {num} Element index location is {result} and number of comparisons {count}")

average_number_of_comparisons_1000_L = comparisons_number_1000_L / n_1000

#############################################################

comparisons_number_100_B = 0

for num in arr_100:
    result,count = binary_search(arr_100,num, 0, len(arr_100)-1)
    comparisons_number_100_B = comparisons_number_100_B + count
    #print(f"For number {num} Element index location is {result} and number of comparisons {count}")

average_number_of_comparisons_100_B = comparisons_number_100_B / n_100


comparisons_number_1000_B = 0

for num in arr_1000:
    result,count = binary_search(arr_1000,num, 0, len(arr_1000)-1)
    comparisons_number_1000_B = comparisons_number_1000_B + count
    #print(f"For number {num} Element index location is {result} and number of comparisons {count}")
 
average_number_of_comparisons_1000_B = comparisons_number_1000_B / n_1000


#############################################################


N = [n_100,n_1000]

average_number_of_comparisons_L = [average_number_of_comparisons_100_L,average_number_of_comparisons_1000_L]
average_number_of_comparisons_L = np.array(average_number_of_comparisons_L)
average_number_of_comparisons_B = [average_number_of_comparisons_100_B,average_number_of_comparisons_1000_B]


plt.figure(figsize=(10,10))
plt.xlabel("Array size N")
plt.ylabel("Average number of comparisons")
plt.plot(N,average_number_of_comparisons_L/55,label="Linear Search",color = "red")
plt.plot(N,average_number_of_comparisons_B,label="Binary Search",color = "blue")
plt.legend(loc="upper left")
plt.show()



