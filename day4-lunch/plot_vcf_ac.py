#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

ac = np.log1p(ac)
fig, ax = plt.subplots()
ax.hist(ac, density=True )
plt.xlabel("Log(Allele Count)")
plt.ylabel("# of identical Allele Counts")
plt.title("Allele Count")
fig.savefig( vcf + ".png" )

fs.close()

