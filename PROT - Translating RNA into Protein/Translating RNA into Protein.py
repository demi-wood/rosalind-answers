'''
A solution to Rosalind's Translating RNA into Protein

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

ID: PROT
Link: http://rosalind.info/problems/prot/
'''

from textwrap import wrap

RNA = open('rosalind_prot.txt').read()

protein = wrap(RNA, 3)

for n, i in enumerate(protein):
    if i == 'UUU' or i == 'UUC':
        protein[n] = 'F'
    elif i == 'UUA' or i == 'UUG' or i == 'CUU' or i == 'CUC' or i == 'CUA' or i == 'CUG':
        protein[n] = 'L'
    elif i == 'UCU' or i == 'UCC' or i == 'UCA' or i == 'UCG' or i == 'AGU' or i == 'AGC':
        protein[n] = 'S'
    elif i == 'UAU' or i == 'UAC':
        protein[n] = 'Y'
    elif i == 'UAA' or i == 'UAG' or i == 'UGA':
        protein[n] = ""
    elif i == 'UGU' or i == 'UGC':
        protein[n] = 'C'
    elif i == 'UGG':
        protein[n] = 'W'
    elif i == 'CCU' or i == 'CCC' or i == 'CCA' or i == 'CCG':
        protein[n] = 'P'
    elif i == 'CAU' or i == 'CAC':
        protein[n] = 'H'
    elif i == 'CAA' or i == 'CAG':
        protein[n] = 'Q'
    elif i == 'CGU' or i == 'CGC' or i == 'CGA' or i == 'CGG' or i == 'AGA' or i == 'AGG':
        protein[n] = 'R'
    elif i == 'AUU' or i == 'AUC' or i == 'AUA':
        protein[n] = 'I'
    elif i == 'AUG':
        protein[n] = 'M'
    elif i == 'ACU' or i == 'ACC' or i == 'ACA' or i == 'ACG':
        protein[n] = 'T'
    elif i == 'AAU' or i == 'AAC':
        protein[n] = 'N'
    elif i == 'AAA' or i == 'AAG':
        protein[n] = 'K'
    elif i == 'GUU' or i == 'GUC' or i == 'GUA' or i == 'GUG':
        protein[n] = 'V'
    elif i == 'GCU' or i == 'GCC' or i == 'GCA' or i == 'GCG':
        protein[n] = 'A'
    elif i == 'GAU' or i == 'GAC':
        protein[n] = 'D'
    elif i == 'GAA' or i == 'GAG':
        protein[n] = 'E'
    elif i == 'GGU' or i == 'GGC' or i == 'GGA' or i == 'GGG':
        protein[n] = 'G'

fprotein = ''.join(protein)

with open('rosalind_prot_sol.txt', 'w') as outfile:
    outfile.write(fprotein)

