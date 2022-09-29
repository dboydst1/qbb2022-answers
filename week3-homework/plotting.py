#!usr/env/bin python

import matplotlib.pyplot as plt
from math import nan, isnan
import numpy as np
import pandas as pd
import allel
from collections import Counter

callset = allel.read_vcf('Effects.vcf', fields=['calldata/GQ', 'calldata/DP', 'variants/AF', 'variants/ANN'], numbers={'variants/AF':1})

dis = []
for i, each in enumerate(callset['variants/ANN']):
    x = each.split('|')
    dis.append(x)

info = []
for i, each in enumerate(dis):
    info.append(each[1])

GQ = []
for i, each in enumerate(callset['calldata/GQ']):
    for number in each:
        GQ.append(number)

GQ_without_nan = [x for x in GQ if isnan(x) == False]

DP = []
for i, each in enumerate(callset['calldata/DP']):
    for number in each:
        DP.append(number)

DP_without_nan = [x for x in DP if isnan(x) == False]

data = Counter(info)
names = list(data.keys())
values = list(data.values())

fig, ax = plt.subplots(nrows = 2, ncols = 2)

ax[0,0].hist(DP_without_nan, bins = 25, range = [0,20])
ax[0,0].set_title('Read Depth Distribution of Variant Genotypes')
ax[0,0].set_ylabel('Count')
ax[0,0].set_xlabel('Read Depth')

ax[0,1].hist(GQ_without_nan, bins = 100, range = [0,75])
ax[0,1].set_title('Quality Distribution of Variant Genotypes')
ax[0,1].set_ylabel('Count')
ax[0,1].set_xlabel('Quality')

ax[1,0].hist(callset['variants/AF'], bins = 20)
ax[1,0].set_title('Allele Frequency Spectrum of Variants')
ax[1,0].set_ylabel('Count')
ax[1,0].set_xlabel('Allele Frequency')

ax[1,1].bar(range(len(data)), values, tick_label=names)
ax[1,1].set_title('Predicted Effect of Variants')
ax[1,1].set_ylabel('Count')
ax[1,1].set_xlabel('Effect')
plt.xticks(rotation=-90)

plt.savefig('Quad_Graphs.png')
plt.show()
plt.close()