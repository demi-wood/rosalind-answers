'''
A solution to Rosalind's Counting Point Mutations

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t). (The number of occurences where the two
samples differ.

ID: HAMM
Link: http://rosalind.info/problems/hamm/
'''

array = []
with open('rosalind_hamm.txt', 'r') as file:
    #takes 2 lines from file, separates into 2 strings
    for line in file:
        line = line.strip()
        array.append(line)

s = array[0]
t = array[1]

#zip iterates through both strings and pairs each value
count = 0
for i, j in zip(s, t):
        if i != j:
            count += 1

print(count)
