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
 
 #the structure of the plots seems to be "L-shaped", and the 1 v 2 and 1 v 3 graphs appear to be mirrored.
 #I think this structure is showing multiple different populations of humans
 
 #Exercise 3
 
 #!/usr/bin/env python

 import sys
 import numpy as np
 import matplotlib.pyplot as plt

 something = np.genfromtxt("joined_stuff", dtype = None, encoding = None, names = ["ID", "SubRegion", "Region", "Sex", "ID2", "pca1", "pca2", "pca3"])


 fig, ax = plt.subplots()
 genders = (np.unique(something["Sex"]))
 for i in genders:
     x = []
     y = []
     for thing in something:
          if i == thing[3]:
             x.append(thing[5])
             y.append(thing[6])
     ax.scatter(x, y, label = i)
 ax.set_xlabel("pca1")
 ax.set_ylabel("pca2")
 ax.set_title("PCA with Gender")
 ax.legend()
 plt.savefig("ex3_c.png")
 plt.show()
 plt.close(fig)

 fig, ax = plt.subplots()
 genders = (np.unique(something["SubRegion"]))
 for i in genders:
     x = []
     y = []
     for thing in something:
          if i == thing[1]:
             x.append(thing[5])
             y.append(thing[6])
     ax.scatter(x, y, label = i)
 ax.set_xlabel("pca1")
 ax.set_ylabel("pca2")
 ax.set_title("PCA with SubRegion")
 ax.legend()
 plt.savefig("ex3_a.png")
 plt.show()
 plt.close(fig)

 fig, ax = plt.subplots()
 genders = (np.unique(something["Region"]))
 for i in genders:
     x = []
     y = []
     for thing in something:
          if i == thing[2]:
             x.append(thing[5])
             y.append(thing[6])
     ax.scatter(x, y, label = i)
 ax.set_xlabel("pca1")
 ax.set_ylabel("pca2")
 ax.set_title("PCA with Region")
 ax.legend()
 plt.savefig("ex3_b.png")
 plt.show()
 plt.close(fig)