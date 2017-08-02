"""
You are given N numbers. Store them in a list and find the second largest number.

Input Format
    The first line contains N. The second line contains an array A[] of N integers each separated by a space.

Constraints
    2 <= N <= 10
    -100 <= A[i] <= 100

Output Format
    Output the value of the second largest number.
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    k = max(arr)
    for i in range(len(arr)):
        if k == max(arr):
            arr.remove(k)
        else:
            j = max(arr)
    print(j)
