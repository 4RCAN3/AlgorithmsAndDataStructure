#This code implements Jump Search which has a worst case complexity of O(√n)
#It works by first checking all items of list, until an item is found that is larger than the search key.
#To find the exact position of the search key in the list a linear search is performed on the sublist L[(k-1)*m, k*m]. Here  k ∈ n, and m is the "block" size

import math

def jump_search(arr, x): # the total number of comparisons in the worst case will be ((n/m) + m-1).
	n=len(arr)
	m=math.sqrt(n)                     # The value of the function ((n/m) + m-1) will be minimum when m = √n. Therefore, the best step size is m = √n.
	prev=0
	while arr[int(min(m, n)-1)] < x:  #in this loop we just jump over indexes by an effective jump(m = √n, proved in above comment)
		prev = m
		m+=m
		if prev>n:
			return -1
	while arr[int(prev)] < x:  #new loop for linear search where we check those positions which were skipped during the above "jumping" loop
		prev+=1
		if prev==min(m, n):
			return -1

	if arr[int(prev)] == x:
		return int(prev)+1

	return -1
  
array = list(map(int, input("Enter the elements of your list: ").split()))
x = int(input("Enter the element to be searched for: "))
result = jump_search(array, x)
if result>-1:
  print("Element found at index: ", result)
else:
  print("Element Not Found!!!")
