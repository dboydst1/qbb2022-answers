#!usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import allel

something = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["ID1", "ID2", "pca1", "pca2", "pca3", "pca4", "pca5", "pca6", "pca7", "pca8", "pca9", "pca10"])

fig, ax = plt.subplots()
ax.scatter(something["pca1"], something["pca2"])
ax.set_ylabel("pca2")
ax.set_xlabel("pca1")
plt.title('PCA Analysis of Genotypes')
plt.show()
plt.savefig("ex2.png")
plt.close(fig)

something2 = np.genfromtxt("plink.frq", dtype = None, encoding = None, names = True)

fig, ax = plt.subplots()
ax.hist(something2["MAF"], bins = 50)
ax.set_ylabel("Counts")
ax.set_xlabel("Allele Frequency")
plt.xticks(np.arange(0, 0.8, step=0.2))
plt.title('Allele Frequency Distribution')
plt.show()
plt.savefig("ex3.png")
plt.close(fig)

something3 = np.genfromtxt("plink.assoc.linear", dtype = None, encoding = None, names = True)


fig, ax = plt.subplots()
pval = -np.log(10**-5)

x = []
xpos = []
y = []
ypos = []
for i,thing in enumerate(something3):
    if pval > -np.log(thing["P"]):
        x.append(thing["P"])
        xpos.append(i)
    if pval <= -np.log(thing["P"]):
        y.append(thing["P"])
        ypos.append(i)
ax.scatter(xpos, -np.log(x))
ax.scatter(ypos, -np.log(y))
ax.set_ylabel("-log10(P-Value)")
ax.set_xlabel("Chromosome Location")
plt.title('Manhattan Plot')
plt.show()
plt.savefig("ex5_b.png")
plt.close(fig)

pvalstore = 1
posstore = 0
for i,thing in enumerate(something3):
    if thing["P"] <= pvalstore:
        pvalstore = thing["P"]
        posstore = i
print(pvalstore)
print(posstore)

IDval = something3[posstore][1]
print(IDval)

callset = allel.read_vcf('genotypes.vcf', fields=['samples','calldata/GT', 'variants/ID'])

dis = []
for i, each in enumerate(callset['variants/ID']):
    dis.append(each)
index = dis.index(IDval)
gt = allel.GenotypeArray(callset['calldata/GT'])

genotype = []
sampleID = []
for i, each in enumerate(gt[index]):
    genotype.append(each)
    sampleID.append(callset['samples'][i])


nogenoindex = []
for i, each in enumerate(genotype):
    if genotype[i][0] == -1:
        nogenoindex.append(i)

something4 = np.genfromtxt("GS451_IC50.txt", dtype = None, encoding = None, names = True)

pheno = []
nophenoindex = []
for i, each in enumerate(something4):
    if each[2] == 'NA':
        each[2] = 0
        nophenoindex.append(i)
    pheno.append(float(each[2]))

for i, each in enumerate(nophenoindex):
    nogenoindex.append(each)
nogenoindex.sort(reverse = True)

for i, each in enumerate(nogenoindex):
    for j, thing in enumerate(sampleID):
        if each == j:
            del sampleID[j]
    for k, item in enumerate(genotype):
        if each == k:
            del genotype[k]
    for l, numb in enumerate(pheno):
        if each == l:
            del pheno[l]

homozygousindex = []
heterozygousindex = []
homozygous_altindex = []
for i, each in enumerate(genotype):
    if genotype[i][0] != genotype[i][1]:
        heterozygousindex.append(i)
    else:
        if genotype[i][0] == 0:
            homozygousindex.append(i)
        if genotype[i][0] == 1:
            homozygous_altindex.append(i)

homozygousdata = []
heterozygousdata = []
homozygous_altdata = []
for i, each in enumerate(pheno):
    for j, thing in enumerate(homozygousindex):
        if i == thing:
            homozygousdata.append(each)
    for k, item in enumerate(heterozygousindex):
        if i == item:
            heterozygousdata.append(each)
    for l, numb in enumerate(homozygous_altindex):
        if i == numb:
            homozygous_altdata.append(each)

fig, ax = plt.subplots()
data = [homozygousdata, heterozygousdata, homozygous_altdata]
ax.boxplot(data)
ax.set_ylabel("Phenotype")
ax.set_xlabel("Genotype")
plt.title('Phenotype Range for Each Genotype')
plt.xticks([1, 2, 3], ['Homozygous', 'Heterozygous', 'Homozygous Alternative'])
plt.show()
plt.savefig("ex6_b.png")
plt.close(fig)
