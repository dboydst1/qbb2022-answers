#usr/bin/env python

import numpy as np
import numpy.lib.recfunctions as rfn
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pickle

#Step 0

input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

col_names = list(input_arr.dtype.names[1:])

row_names = []
for i, each in enumerate(input_arr):
    row_names.append(each[0])
row_names = np.reshape(row_names, (34718,))

FPKMdata =  []
for i, each in enumerate(input_arr):
    for j, thing in enumerate(each):
        if j > 0:
            FPKMdata.append(thing)

x = np.reshape(FPKMdata, (34718, 10))

nonzerorows = []
zerorows = []
for i, each in enumerate(np.median(x, axis = 1)):
    if each > 0:
        nonzerorows.append(i)
    elif each == 0:
        zerorows.append(i)

x = x[nonzerorows]
row_names = row_names[nonzerorows]

x = np.log2(x + 0.1)
tx = x.T

#Step 1

# linkx = sp.cluster.hierarchy.linkage(x)
# leavesx = sp.cluster.hierarchy.leaves_list(linkx)
# xreorder = [x[i] for i in leavesx]
# row_names_reorder = [row_names[i] for i in leavesx]
# xreorder = np.array([element for (i,element) in enumerate(xreorder)])
#
# txreorder = xreorder.T
#
# linktx = sp.cluster.hierarchy.linkage(txreorder)
# leavestx = sp.cluster.hierarchy.leaves_list(linktx)
# txreorder = [txreorder[i] for i in leavestx]
# col_names_reorder = [col_names[i] for i in leavestx]
# txreorder = np.array([element for (i,element) in enumerate(txreorder)])
#
# heatmapdata = txreorder.T
#
# sns.heatmap(heatmapdata).set(title='Clustered Gene Expression Data', xlabel='Animal', ylabel='Gene')
# plt.savefig('heatmap.png')
# plt.close()
#
# sp.cluster.hierarchy.dendrogram(linktx, orientation = 'bottom')
# plt.savefig('dendrogram.png')
# plt.close()

#Step 2

sexes = []
stages = []

for l in col_names:
    sexes.append(l.split('_')[0])
    stages.append(l.split('_')[1])


betavals = []
pvals = []
for i in range(x.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names)):
        list_of_tuples.append((row_names[i], x[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    results = sm.OLS.from_formula(data = longdf, formula = 'fpkm ~ stage').fit()
    pvals.append(results.pvalues[0])
    betavals.append(results.params[0])

# sm.qqplot(np.array(pvals), line = '45', dist = sp.stats.uniform)
# plt.tight_layout()
# plt.savefig("qqplot.png")
# plt.close()

tenperc = sm.stats.multipletests(pvals, alpha = 0.1, method = "fdr_bh")
tflist = tenperc[0]
significant = row_names[tflist]

# with open("nosexlist.md", "w") as outfile:
#     outfile.write("\n".join(significant))

sexbetavals = []
sexpvals = []
for i in range(x.shape[0]):
    list_of_sextuples = []
    for j in range(len(col_names)):
        list_of_sextuples.append((row_names[i], x[i,j], sexes[j], stages[j]))
    longdfsex = np.array(list_of_sextuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    sexresults = sm.OLS.from_formula(data = longdfsex, formula = 'fpkm ~ stage + sex').fit()
    sexpvals.append(sexresults.pvalues[0])
    sexbetavals.append(sexresults.params[0])

sextenperc = sm.stats.multipletests(sexpvals, alpha = 0.1, method = "fdr_bh")
sextflist = sextenperc[0]
sexsignificant = row_names[sextflist]

# with open("sexlist.md", "w") as outfile:
#     outfile.write("\n".join(sexsignificant))

overlap = set(significant) & set(sexsignificant)
percent = len(overlap) / len(significant) * 100
# print(percent)

color = []
for thing in sextflist:
	if thing == True:
		color.append("green")
	elif thing == False:
		color.append("black")

fig, ax = plt.subplots()
ax.scatter(sexbetavals, -np.log10(sexpvals), color = color)
ax.set_ylabel("-log10(p-values)")
ax.set_xlabel("beta values")
ax.set_title("FDR ~ stage + sex")
fig.savefig("volcano.png")
