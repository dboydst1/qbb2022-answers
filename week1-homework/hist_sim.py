#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

readstart = np.random.randint(0, high=999900, size = 50000, dtype = int)

histarray = np.zeros(1000000, dtype = int)

for i, num in enumerate(readstart):
    for j in range(0,100):
        histarray[num + j] += 1

counter = 0
for i, num in enumerate(histarray):
    if num == 0:
        counter += 1
print(counter)
        
poisdis = np.random.poisson(lam=5, size = 1000000)

counterpois = 0
for i, num in enumerate(poisdis):
    if num == 0:
        counterpois += 1
print(counterpois)

fig, ax = plt.subplots()
ax.hist(histarray, alpha=0.5, bins = 10)
ax.hist(poisdis, alpha=0.5, bins = 10)
ax.set_ylabel("Number of Reads")
ax.set_xlabel("Read Depth")
plt.title("Read Depth Compared to Poisson Distribution")
plt.savefig("ex1.2.png")
plt.show()
plt.close(fig)


np.random.seed(4)

readstart = np.random.randint(0, high=999900, size = 150000, dtype = int)

histarray = np.zeros(1000000, dtype = int)

for i, num in enumerate(readstart):
    for j in range(0,100):
        histarray[num + j] += 1

counter = 0
for i, num in enumerate(histarray):
    if num == 0:
        counter += 1
print(counter)
        
poisdis = np.random.poisson(lam=15, size = 1000000)

counterpois = 0
for i, num in enumerate(poisdis):
    if num == 0:
        counterpois += 1
print(counterpois)

fig, ax = plt.subplots()
ax.hist(histarray, alpha=0.5, bins = 10)
ax.hist(poisdis, alpha=0.5, bins = 10)
ax.set_ylabel("Number of Reads")
ax.set_xlabel("Read Depth")
plt.title("Read Depth Compared to Poisson Distribution")
plt.savefig("ex1.4.png")
plt.show()
plt.close(fig)
