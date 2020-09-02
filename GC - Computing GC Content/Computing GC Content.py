'''
A solution to Rosalind's Computing GC Content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.

ID: GC
Link: http://rosalind.info/problems/GC/
'''

from Bio import SeqIO

seqID = []
seq = []
with open('rosalind_gc.txt', 'r') as f:
    for i in SeqIO.parse(f, "fasta"):
        seqID.append(str(i.id))
        seq.append(str(i.seq))

GCContent = []
for string in seq:
    GCContent.append(float((string.count('G') + string.count('C'))) / len(string) * 100)
    highestGC = max(GCContent)
    highestGCindex = GCContent.index(highestGC)

with open('rosalind_gc_sol.txt', 'w') as outfile:
    outfile.write(seqID[highestGCindex] + '\n')
    outfile.write(str(highestGC))


