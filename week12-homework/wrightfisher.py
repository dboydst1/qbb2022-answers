#usr/bin/env python

#use: Population, allele frequency

import numpy as np
import sys
import matplotlib.pyplot as plt
import statistics
import seaborn as sns


population = int(sys.argv[1])
allele_count = population*2
allele_frequency = float(sys.argv[2])
probability = allele_frequency

def simulation(allele_c, probab):
    freqlist = []
    while probab != 1 and probab != 0:
        ac = np.random.binomial(n = allele_c, p = probab)
        freq = ac/allele_c
        freqlist.append(freq)
        allele_c = ac
        probab = float(freq)
    return(freqlist)

first_sim = simulation(allele_count, probability)

def freqplot(freqlist, pltsave = False, name = 'plt.png'):
    fig, ax = plt.subplots()
    ax.plot(range(0,len(freqlist)),freqlist)
    plt.xlabel('Generations')
    plt.ylabel('Allele Frequency')
    plt.text(0, 0, s = ('Starting Population = ' + str(population) + '. Starting AF = ' + str(probability)), fontsize = 10)
    if pltsave == True:
        plt.savefig(name)
    plt.show()
    plt.close()

freqplot(first_sim, True, 'allelefreq.png')

ttg = []
for each in range(0,1000):
    simulation(allele_count, probability)
    ttg.append(len(freqlist))
fig, ax = plt.subplots()
ax.hist(ttg, bins = 50)
plt.title('Generations Until Fixation')
plt.xlabel('Number of Generations')
plt.ylabel('Count')
plt.savefig('GentilFixation.png')
plt.close()

ttgavgs = []

ttg100 = []
for each in range(0,100):
    pop100 = simulation(100*2, probability)
    ttg100.append(len(pop100))

ttg500 = []
for each in range(0,500):
    pop500 = simulation(500*2, probability)
    ttg500.append(len(pop500))

ttg1000 = []
for each in range(0,1000):
    pop1000 = simulation(1000*2, probability)
    ttg1000.append(len(pop1000))

ttg5000 = []
for each in range(0,5000):
    pop5000 = simulation(5000*2, probability)
    ttg5000.append(len(pop5000))

ttg10000 = []
for each in range(0,10000):
    pop10000 = simulation(10000*2, probability)
    ttg10000.append(len(pop10000))

ttg50000 = []
for each in range(0,50000):
    pop50000 = simulation(50000*2, probability)
    ttg50000.append(len(pop50000))

ttgavgs.extend([statistics.fmean(ttg100), statistics.fmean(ttg500), statistics.fmean(ttg1000), statistics.fmean(ttg5000), statistics.fmean(ttg10000), statistics.fmean(ttg50000)])

sizes = [100, 500, 1000, 5000, 10000, 50000]
sizes = np.log10(sizes)

fig, ax = plt.subplots()
ax.plot(sizes, ttgavgs)
plt.title('Generations until Fixation for Differing N Simulations')
plt.xlabel('log10(Number of Simulations)')
plt.ylabel('Average Generations until Fixation')
plt.savefig('NFixation.png')
plt.show()
plt.close()


ttg2alleles = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]

listoflists = []
for thing in ttg2alleles:
    thinglist = []
    for each in range(0,100):
        sim = simulation(100*2, thing)
        thinglist.append(len(sim))
    listoflists.append(thinglist)

fig, ax = plt.subplots()
g = sns.stripplot(data = listoflists)
g.set_xticks(range(len(listoflists)))
g.set_xticklabels(['0.25', '0.3', '0.35', '0.4', '0.45', '0.5', '0.55', '0.6', '0.65', '0.7', '0.75'])
plt.xlabel('Allele Frequency')
plt.ylabel('Generations Until Fixation')
plt.text(0, 25, s = ('Starting Population = 100'))
plt.title('Generations until Fixation for Different Starting Allele Frequencies')
plt.savefig('allelefixation.png')
plt.show()
plt.close()