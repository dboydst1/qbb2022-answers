#!/usr/bin/env python

#usage: python globalalign.py file.faa scoring-matrix.txt gap-penalty save-file.txt

import sys
from fasta import readFASTA
import numpy as np
import csv

# note that I am aware this code is very inefficient... I'm having some issues with the lab I am rotating in over-working me. Working on fixing it.
# the code runs with the DNA sequence, and I got it to run with Amino acids and I don't know what I changed, but now it does not run with the AA.
# I could use some help with that... I think it has something to do with the orderlist and the sequence not being the same type (one is np.str and the other is str).

# sequence1 = 'TGTTACGG'
# sequence2 = 'GGTTGACTA'

filename = sys.argv[1]

with open(filename) as f:
    reader = csv.reader(f, delimiter=' ')
    first_row = next(reader)
    num_cols = len(first_row)

scoring_matrix = np.loadtxt(sys.argv[2], usecols=range(num_cols), dtype = 'str')
print(scoring_matrix)

input_sequences = readFASTA(open(filename))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]


# sequence1 = 'TACGATTA'
# sequence2 = 'ATTAACTTA'

input_sequences = readFASTA(open(filename))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))

gap_penalty = float(sys.argv[3])

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1), int)
Traceback = np.zeros((len(sequence1)+1, len(sequence2)+1), int)

for i in range(len(sequence1)+1):
    F_matrix[i,0] = i*gap_penalty
    Traceback[i,0] = 1

for j in range(len(sequence2)+1):
    F_matrix[0,j]=j*gap_penalty
    Traceback[0,j] = 3

orderlist = scoring_matrix[0]
print(orderlist)

    
for i in range(1, len(sequence1)+1): # loop through rows
    for j in range(1, len(sequence2)+1): # loop through columns
        if sequence1[i-1] == sequence2[j-1]: # if sequence1 and sequence2 match at positions i and j, respectively...
            for  k, item in enumerate(orderlist):
                if sequence1[i-1] == item:
                    match_score = int(scoring_matrix[k,k])
                    d = F_matrix[i-1, j-1] + match_score
        else: # if sequence1 and sequence2 don't match at those positions...
            for k, item in enumerate(orderlist):
                if sequence1[i-1] == item:
                    for o, thing in enumerate(orderlist):
                        if sequence2[j-1] == thing:
                            mismatch_score = int(scoring_matrix[k,o])
                            d = F_matrix[i-1, j-1] + mismatch_score
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty
        F_matrix[i,j] = max(d,h,v)
        if d>v and d>h:
            Traceback[i,j]=2
        elif h>v and h>d:
            Traceback[i,j]=3
        elif v>h and v>d:
            Traceback[i,j]=1
        else:
            Traceback[i,j]=5
        if int(Traceback[i,j]) == 5:
            if d==v or d==h:
                Traceback[i,j]=2
            elif v==h:
                Traceback[i,j]=3
print(F_matrix)
print(Traceback)

seq1align = []
seq2align = []

a = F_matrix.shape[0]-1
b = F_matrix.shape[1]-1

alignment_score=F_matrix[a,b]

seq1gaps = 0
seq2gaps = 0

while a+b>0:
    if int(Traceback[a,b]) == 2:
        seq1align.append(sequence1[a-1])
        seq2align.append(sequence2[b-1])
        a -= 1
        b -= 1
    elif int(Traceback[a,b]) == 3:
        seq1align.append('-')
        seq2align.append(sequence2[b-1])
        seq2gaps += 1
        b -= 1
    elif int(Traceback[a,b]) == 1:
        seq1align.append(sequence1[a-1])
        seq2align.append('-')
        seq1gaps += 1
        a -= 1

seq1align.reverse()
seq2align.reverse()

str1=''
alignment1 = str1.join(seq1align)
alignment2 = str1.join(seq2align)
print("sequence 1 has " + str(seq1gaps) + " gaps")
print("sequence 2 has " + str(seq2gaps) + " gaps")
print("alignment score = " + str(alignment_score))
print(alignment1)
print(alignment2)

filepath = open(sys.argv[4],'w')
filepath.write("Seq_1:"+alignment1+"\n"+"Seq_2:"+alignment2)
filepath.close()

