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
    
    in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1
    filteredfrags = []
    for i, each in enumerate(frags):
        if each[3] > 343067 and each [3] < 343208:
            filteredfrags.append(each)
    filtdata1 = []
    for i, each in enumerate(data1):
        if each[1] > 343067 and each [1] < 343208:
            if each[0] > 343067 and each [0] < 343208:
                filtdata1.append(each)
    filtdata2 = []
    for i, each in enumerate(data2):
        if each[1] > 343067 and each [1] < 343208:
            if each[0] > 343067 and each [0] < 343208:
                filtdata2.append(each)
    
    for i, each in enumerate(filtdata1):
        each[2] = numpy.log(each[2])
    for i, each in enumerate(filtdata2):
        each[2] = numpy.log(each[2])
    
    minimum1 = 10000
    for i, each in enumerate(filtdata1):
        if each[2] < minimum1:
            minimum1 = each[2]
    for i, each in enumerate(filtdata1):
        each[2] = each[2] - minimum1
    
    minimum2 = 10000
    for i, each in enumerate(filtdata2):
        if each[2] < minimum2:
            minimum2 = each[2]
    for i, each in enumerate(filtdata2):
        each[2] = each[2] - minimum2
    
    mat = numpy.zeros((140,140))
    for i, each in enumerate(filtdata1):
        mat[each[0]-343068,each[1]-343068] = each[2]
        mat[each[1]-343068,each[0]-343068] = each[2]
    
    
    mat2 = numpy.zeros((140,140))
    for i, each in enumerate(filtdata2):
        mat2[each[0]-343068,each[1]-343068] = each[2]
        mat2[each[1]-343068,each[0]-343068] = each[2]
    
    # columnnames = []
    # rownames = []
    # data1values = []
    # for i, each in enumerate(data1):
        # columnnames.append(each[0])
        # rownames.append(each[1])
        # data1values.append(each[2])
    fig, ax = plt.subplots(1,3)
    
    sns.heatmap(mat, ax = ax[0], cmap = "magma")
    ax[0].set_title("dCTCF + transgene")
    ax[0].axes.xaxis.set_ticklabels([])
    ax[0].axes.yaxis.set_ticklabels([])
    
    sns.heatmap(mat2, ax = ax[1], cmap = "magma")
    ax[1].set_title("ddCTCF + transgene")
    ax[1].axes.xaxis.set_ticklabels([])
    ax[1].axes.yaxis.set_ticklabels([])
    
    mat = remove_dd_bg(mat)
    mat = smooth_matrix(mat)
    mat2 = remove_dd_bg(mat2)
    mat2 = smooth_matrix(mat2)
    mat3 = mat - mat2
    
    sns.heatmap(mat3, ax = ax[2], cmap = "seismic")
    ax[2].set_title("Differential Map")
    ax[2].axes.xaxis.set_ticklabels([])
    ax[2].axes.yaxis.set_ticklabels([])
    plt.savefig('full_data.png')
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()