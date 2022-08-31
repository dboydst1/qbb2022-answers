 # QBB2022 - Day 3 - Homework Exercises Submission
 
 #Exercise 1
 
 plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3 #code used for the pca
 
 #Exercise 2
 
 #!/usr/bin/env python

 import sys
 import numpy as np
 import matplotlib.pyplot as plt

 fname = sys.argv[1]

 something = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["ID1", "ID2", "pca1", "pca2", "pca3"])

 fig, ax = plt.subplots()
 ax.scatter(something["pca1"], something["pca2"])
 ax.set_ylabel("pca2")
 ax.set_xlabel("pca1")
 plt.savefig("ex2_a.png")
 plt.close(fig)

 fig, ax = plt.subplots()
 ax.scatter(something["pca1"], something["pca3"])
 ax.set_ylabel("pca3")
 ax.set_xlabel("pca1")
 plt.savefig("ex2_b.png")
 plt.close(fig)
 
 #