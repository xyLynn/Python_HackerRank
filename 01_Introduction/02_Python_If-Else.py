"""
Input Format
	A single line containing a positive integer, n.

Constraints
	1 <= n <= 100

Output Format
	Print Weird if the number is 'Weird'; otherwise, print 'Not Weird'.

"""
if __name__ == '__main__':
    n = int(input())
    if n in range(6, 21):
    	print('Weird')
    else:
    	if n % 2 == 1:
    		print('Weird')
    	else:
    		print('Not Weird')