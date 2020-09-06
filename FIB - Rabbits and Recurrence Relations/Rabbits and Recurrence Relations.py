'''
A solution to Rosalind's Rabbits and Recurrence Relations.

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months,
if we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

ID: FIB
Link: http://rosalind.info/problems/fib/
'''

with open('rosalind_fib.txt', 'r') as file:
    for line in file:
        numbers = line.split()

n = int(numbers[0])
k = int(numbers[1])

def rabbitRecurrence(n, k):
    """
        Find the number of rabbits there will be after n months if k rabbits are
        born each generation.
        ----------
        n : int
            The number of months.
        k : int
            The number of children each adult rabbit has each generation.
    """
    if n < 1:
        return 0
    elif n > 40:
        print("The number of months must be 40 or less to follow the Rosalind problem.")
    elif n == 1 or n == 2:
        return 1
    elif k > 5:
        print("The number of children a rabbit can have must be 5 or less to follow the Rosalind problem.")
    else:
        return(rabbitRecurrence(n-1, k) + rabbitRecurrence(n-2, k)*k)
    
print(str(rabbitRecurrence(n, k)))

'''
Note: This problem was difficult to understand and so I used the following web
pages to understand what the problem was asking for and using recurrence to find
numbers in the Fibonacci sequence:

https://medium.com/algorithms-for-life/rosalind-walkthrough-rabbits-and-recurrence-relations-4812c0c2ddb3

https://chrispresso.coffee/2019/02/21/rosalind-rabbits-and-recurrence-relations/

https://www.javatpoint.com/python-display-fibonacci-sequence-recursion#:~:text=Python%20Program%20to%20Display%20Fibonacci%20Sequence%20Using%20Recursion&text=A%20Fibonacci%20sequence%20is%20a,def%20recur_fibo(n)%3A
'''
