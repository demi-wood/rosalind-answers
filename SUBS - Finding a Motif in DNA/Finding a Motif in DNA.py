'''
A solution to Rosalind's Finding a Motif in DNA

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

ID: SUBS
Link: http://rosalind.info/problems/subs/
'''

array = []
with open('rosalind_subs.txt', 'r') as file:
    #takes 2 lines from file, separates into 2 arrays
    for line in file:
        line = line.strip()
        array.append(line)

s = array[0]
t = array[1]

#finds occurences of t in s
i = 0
occurences = []
while i < len(s):
    i = s.find(t, i)
    if i == -1:
        break
    i+=1

    #adds the motifs to an array
    occurences.append(i)

with open('rosalind_subs_sol.txt', 'w') as outfile:
    for item in occurences:
        outfile.write(str(item) + ' ')
