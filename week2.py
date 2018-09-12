'''
1. Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.

Here are some examples of how your function should work.

  >>> intreverse(783)
  387
  >>> intreverse(242789)
  987242
  >>> intreverse(3)
  3
  '''
 def intreverse(n):
	rev = 0    
	while(n > 0):  
		rem = n %10    
		rev = (rev *10) + rem    
		n = n //10  
	return rev

'''
2. Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.

Here are some examples to show how your function should work.

 
  >>> matched("zb%78")
  True
  >>> matched("(7)(a")
  False
  >>> matched("a)*(?")
  False
  >>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
  True
  '''
def matched(s):
    count = 0
    for i in s :
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0  

'''
3. Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.

  >>> sumprimes([3,3,1,13])
  19
  >>> sumprimes([2,4,6,9,11])
  13
  >>> sumprimes([-3,1,6])
  0
  '''
def sumprimes(l):
	primeNum = []
	for item in l:
	    is_prime = True
	    if(item >= 2):
	        maxInt = int(item ** 0.5) + 1
	        for i in range(2, maxInt):
	            if(item % i == 0):
	                is_prime = False
	                break
	        if(is_prime):
	            primeNum.append(item)
	return(sum(primeNum))