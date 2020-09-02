'''
A solution to Rosalind's Complemtnting a Strand of DNA

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

ID: REVC
Link: http://rosalind.info/problems/revc/
'''

from Bio.Seq import Seq

with open('rosalind_revc.txt', 'r') as file:
    string = Seq(file.read())
    rComp = string.reverse_complement()

with open('rosalind_revc_sol.txt', 'w') as outfile:
    outfile.write(str(rComp))



'''
#this was the first solution created for this problem

with open('rosalind_revc.txt', 'r') as file:
    string = file.read()
    rString = string[::-1]
    
rString = rString.replace('A', '1').replace('C', '2').replace('G', '3').replace('T', '4')
rString = rString.replace('1', 'T').replace('2', 'G').replace('3', 'C').replace('4', 'A')

print(rString)
'''
