'''
A solution to Rosalind's Mendel's First Law.

Given: Three positive integers k, m, and n, representing a population containing
k+m+n organisms: k individuals are homozygous dominant for a factor, m are
heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will
produce an individual possessing a dominant allele (and thus displaying the
dominant phenotype). Assume that any two organisms can mate.

ID: IPRB
Link: http://rosalind.info/problems/iprb/
'''

with open('rosalind_iprb.txt', 'r') as file:
    for line in file:
        organisms = line.split()

k = int(organisms[0])
m = int(organisms[1])
n = int(organisms[2])

def mendelFirstLaw(k, m, n):

    pop = k + m + n

    # 1st parent = k
    kk = (k/pop) * ((k-1)/(pop-1)) * 1
    km = (k/pop) * (m/(pop-1)) * 1
    kn = (k/pop) * (n/(pop-1)) * 1

    # 1st parent = m
    mk = (m/pop) * (k/(pop-1)) * 1
    mm = (m/pop) * ((m-1)/(pop-1)) * 0.75
    mn = (m/pop) * (n/(pop-1)) * 0.5

    #1st parent = n
    nk = (n/pop) * (k/(pop-1)) * 1
    nm = (n/pop) * (m/(pop-1)) * 0.5
    nn = (n/pop) * ((n-1)/(pop-1)) * 0

    prob = kk+km+kn+mk+mm+mn+nk+nm+nn
    print(prob)

mendelFirstLaw(k, m, n)
