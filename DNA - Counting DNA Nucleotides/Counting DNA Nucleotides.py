'''
A solution to Rosalind's Counting DNA Nucleotides

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in s.

ID: DNA
Link: http://rosalind.info/problems/dna/
'''

with open('rosalind_dna.txt', 'r') as file:
    string = file.read()

A = string.count ('A')
C = string.count ('C')
G = string.count ('G')
T = string.count ('T')

print(A, C, G, T)
