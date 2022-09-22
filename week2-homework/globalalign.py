#!/usr/bin/env python

import sys
from fasta import readFASTA
import numpy as np

# sequence1 = 'TGTTACGG'
# sequence2 = 'GGTTGACTA'

filename = sys.argv[1]

scoring_matrix = np.loadtxt(sys.argv[2], usecols=range(5), dtype = 'str')
print(scoring_matrix)


# for i, item in enumerate(scoring_matrix):
#     print(item)
#     print(scoring_matrix[0,0])
    # for j in item:
#        print(j)
#        if j == item[0:range(scoring_matrix)][0]

input_sequences = readFASTA(open(filename))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))

sequence1 = 'TACGATTA'
sequence2 = 'ATTAACTTA'

gap_penalty = float(sys.argv[3])

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))

for i in range(len(sequence1)+1):
	F_matrix[i,0] = i*gap_penalty

for j in range(len(sequence2)+1):
	F_matrix[0,j] = j*gap_penalty

orderlist = scoring_matrix[0]
print(orderlist)

    
for i in range(1, len(sequence1)+1): # loop through rows
    for j in range(1, len(sequence2)+1): # loop through columns
        if sequence1[i-1] == sequence2[j-1]: # if sequence1 and sequence2 match at positions i and j, respectively...
            for  k, item in enumerate(orderlist):
                if sequence1[i-1] == item:
                    match_score = float(scoring_matrix[k,k])
                    d = F_matrix[i-1, j-1] + match_score
        else: # if sequence1 and sequence2 don't match at those positions...
            for k, item in enumerate(orderlist):
                if sequence1[i-1] == item:
                    for o, thing in enumerate(orderlist):
                        if sequence2[j-1] == thing:
                            mismatch_score = float(scoring_matrix[k,o])
                            d = F_matrix[i-1, j-1] + mismatch_score
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty

        F_matrix[i,j] = max(d,h,v)
print(F_matrix)

q = max(len(sequence1), len(sequence2))
print(q)
seq1align = []
seq2align = []
while q >= 0:
    if q == max(len(sequence1), len(sequence2)):
        x = F_matrix.shape[1]-1
        y = F_matrix.shape[0]-1
        if F_matrix[y,x] >= min(F_matrix[y,x-1], F_matrix[y-1,x]):
            seq1align.append(sequence1[y-1])
            seq2align.append(sequence2[x-1])
    # elif len(sequence1) == len(sequence2):
#         if F_matrix[q,q]
#     elif len(sequence1) > len(sequence2):
#     elif len(sequence1) < len(sequence2):
    q -= 1


# for row_index in range(scoring_matrix.shape[0]): # The number of rows is the first value in .shape
#     for col_index in range(scoring_matrix.shape[1]): # The number of columns is the second value in .shape
#         print(scoring_matrix[row_index, col_index])
        
#
# filepath = sys.argv[4]

input_sequences = readFASTA(open(filename))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))

