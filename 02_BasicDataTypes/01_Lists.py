"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through
each command in order and perform the corresponding operation on your list.

Input Format
	The first line contains an integer, n, denoting the number of commands. 
	Each line i of the n subsequent lines contains one of the commands described above.

Constraints
	The elements added to the list must be integers.

Output Format
	For each command of type print, print the list on a new line.
"""
if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(1, N+1):
        linput = input()
        s = linput.split() 	    	
        if s[0] == 'insert':
            	l.insert(int(s[1]), int(s[2]))
        elif s[0] == 'print':
            	print(l)
        elif s[0] == 'remove':
        		l.remove(int(s[1]))
        elif s[0] == 'append':
        		l.append(int(s[1]))
        elif s[0] == 'sort':
        		l.sort()
        elif s[0] == 'pop':
        		l.pop()
        elif s[0] == 'reverse':
        		l.reverse()



