'''
#
1. Define a Python function descending(l) that returns True if each element in its input list is at most as big as the one before it. For instance:

  >>> descending([])
  True

  >>> descending([4,4,3])
  True

  >>> descending([19,17,18,7])
  False
#'''

def descending(l):
	i=0
	if l == []:
		return True
	while(i < len(l)-1):
		if l[i] >= l[i+1]:
			i=i+1
		else:
			return False
	return True

'''
2.	A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of strictly increasing values. The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing sequence is the first value of the increasing sequence.

	Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise.

	Here are some examples to show how your function should work.

	  >>> valley([3,2,1,2,3])
	  True

	  >>> valley([3,2,1])
	  False

	  >>> valley([3,3,2,1,2])
	  False
'''

def valley(l):
	i = 0
	a = 0
	j = 0
	while(i < len(l)-1):
		if(l[i] > l[i+1]):
			i += 1
			j=i
		else:
			break
	while(j < len(l)-1):
		if(l[j] < l[j+1]):
			j += 1
			a=j
		else:
			break
	if a+1 == len(l) and len(l) >= 2:
		return True
	else:
		return False
	

'''
3. A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

  1  2  3
  4  5  6 
would be represented as [[1, 2, 3], [4, 5, 6]].

The transpose of a matrix makes each row into a column. For instance, the transpose of the matrix above is

  1  4  
  2  5
  3  6
Write a Python function transpose(m) that takes as input a two dimensional matrix using this row-wise representation and returns the transpose of the matrix using the same representation.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

  >>> transpose([[1,4,9]])
  [[1], [4], [9]]

  >>> transpose([[1,3,5],[2,4,6]])
  [[1, 2], [3, 4], [5, 6]]

  >>> transpose([[1,1,1],[2,2,2],[3,3,3]])
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
  '''
def transpose(l):
	a=[]
	b=[]

	for j in range(0,len(l[0])):
		for k in range(0,len(l)):
			a.append(l[k][j])
		b.append(a)
		a=[]
	
	return b


l = []
result1 = descending(l)
print(result1)


l = [4,3,2,1]
result2 = valley(l)
print(result2)


l = [[1,2,3]]
result3 = transpose(l)
print(l)
print(result3)
