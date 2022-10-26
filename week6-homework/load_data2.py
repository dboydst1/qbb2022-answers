#!/usr/bin/env python

import sys
import seaborn as sns
import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = numpy.copy(mat)
    for i in range(N):
        bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
        mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
        if i > 0:
            mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
    return mat2

def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat

def main():
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
    in1_fname, bin_fname, out_fname = sys.argv[1:4]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 10400000
    end = 13400000
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1
    filteredfrags = []
    for i, each in enumerate(frags):
        if each[3] > 54878 and each [3] < 54951:
            filteredfrags.append(each)
    filtdata1 = []
    for i, each in enumerate(data1):
        if each[1] > 54878 and each [1] < 54951:
            if each[0] > 54878 and each [0] < 54951:
                filtdata1.append(each)
    
    for i, each in enumerate(filtdata1):
        each[2] = numpy.log(each[2])
    
    minimum1 = 10000
    for i, each in enumerate(filtdata1):
        if each[2] < minimum1:
            minimum1 = each[2]
    for i, each in enumerate(filtdata1):
        each[2] = each[2] - minimum1
    
    mat = numpy.zeros((72,72))
    for i, each in enumerate(filtdata1):
        mat[each[0]-54878,each[1]-54878] = each[2]
        mat[each[1]-54878,each[0]-54878] = each[2]
    print(mat)
    
    meanmat = numpy.zeros((72,72))
    for i, thing in enumerate(mat):
        meanmat[i] = numpy.mean(mat[(i - 5):i, i:(i + 5)])
    print(meanmat)
    
    fig, ax = plt.subplots(2,1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
    
    sns.heatmap(mat, ax = ax[0], cmap = "magma")
    ax[0].set_title("Pre-insulation Score Interactions")
    ax[0].axis('off')
    plt.margins(x=0)
    
    sns.heatmap(meanmat, ax = ax[1], cmap = "magma")
    ax[1].set_title("Insulation Scores")
    ax[1].axis('off')
    plt.margins(x=0)
    
    plt.savefig('insulation.png')
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()