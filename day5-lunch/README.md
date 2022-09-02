 # qbb2022 day5 lunch
 
 #Exercise 1
 
 # First extract the mother and father counts with the ID:
 
awk 'BEGIN{FS=","; OFS="\t"} /father/ {$1=$1; print $5, $6}' aau1043_dnm.csv | sort | uniq -c > fathers.txt
awk 'BEGIN{FS=","; OFS="\t"} /mother/ {$1=$1; print $5, $6}' aau1043_dnm.csv | sort | uniq -c > mothers.txt

 # combine files and sort by ID. Columns are "count, ID, Paternal"

join -1 2 -2 2 fathers.txt mothers.txt | cut -f 1,2,4 -d ' ' | sort > combined.txt

 # sort age file
 
awk 'BEGIN{FS=","; OFS=" "} {$1=$1; print}' aau1043_parental_age.csv | sort > ages.txt

join combined.txt ages.txt > final.txt

 #Exercise 2
 
 #!/usr/bin/env python

 import numpy as np
 import matplotlib.pyplot as plt
 import statsmodels.formula.api as smf
 import statsmodels.api as sm
 from scipy import stats

 df = np.genfromtxt("Final.txt", delimiter = " ", dtype = None, encoding = None, names = ["probandID", "Father_count", "Mother_count", "Father_age", "Mother_age"])

 fig, ax = plt.subplots()
 ax.scatter(df["Mother_count"], df["Mother_age"])
 ax.set_xlabel("Number of Inherited de novo Mutations")
 ax.set_ylabel("Age of Mother")
 ax.set_title("Maternally Inherited de novo Mutations with Age")
 plt.show()

 fig, ax = plt.subplots()
 ax.scatter(df["Father_count"], df["Father_age"])
 ax.set_xlabel("Number of Inherited de novo Mutations")
 ax.set_ylabel("Age of Father")
 ax.set_title("Paternally Inherited de novo Mutations with Age")
 plt.show()
 