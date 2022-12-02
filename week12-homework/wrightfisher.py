#usr/bin/env python

#use: Allele Count, probability of selecting that Allele (allele count/population)

import numpy as np
import sys
import matplotlib.pyplot as plt


population = int(sys.argv[1])
allele_count = population*2
allele_frequency = float(sys.argv[2])
probability = allele_frequency

freqlist = []
lastac = allele_count

def simulation(allele_count, probability):
    while probability != 1 and probability != 0:
        ac = np.random.binomial(n = allele_count, p = probability)
        freq = ac/allele_count
        freqlist.append(freq)
        allele_count = ac
        probability = float(freq)

simulation(allele_count, probability)

def freqplot(pltsave = False, name = 'plt.png'):
    fig, ax = plt.subplots()
    ax.plot(range(0,len(freqlist)),freqlist)
    plt.xlabel('Generations')
    plt.ylabel('Allele Frequency')
    plt.text(0, 0, s = ('Starting Population = ' + str(population) + '. Starting AF = ' + str(probability)), fontsize = 10)
    if pltsave == True:
        plt.savefig(name)
    plt.close()

# freqplot(True, 'allelefreq.png')

# ttg = []
# for each in range(0,1000):
#     simulation(allele_count, probability)
#     ttg.append(len(freqlist))
# fig, ax = plt.subplots()
# ax.hist(ttg, bins = 50)
# plt.title('Generations Until Fixation')
# plt.xlabel('Number of Generations')
# plt.ylabel('Count')
# plt.savefig('GentilFixation.png')
# plt.close()


