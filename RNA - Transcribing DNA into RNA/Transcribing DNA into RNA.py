'''
A solution to Rosalind's Transcribing DNA into RNA

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t ('A', 'C', 'G', 'U').

ID: RNA
Link: http://rosalind.info/problems/rna/
'''

with open('rosalind_rna.txt', 'r') as file:
    string = file.read()

string = string.replace('T', 'U')

with open('rosalind_rna_sol.txt', 'w') as outfile:
        outfile.write(string)
