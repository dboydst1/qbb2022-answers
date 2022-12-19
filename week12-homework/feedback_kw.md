## Week 13

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10 out of 10 points possible

1. Wright Fisher simulation is a function

2. simulation uses starting allele frequency and population size as input

3. simulation uses `numpy.random.binomial` to draw allele count samples

4. simulation stops when one allele is fixed

5. simulation returns a list of allele frequencies at each generation

6. line plot generation number x-axis and allele frequency y-axis with notated starting allele frequency and pop size as well as labeled axes; 0.5 pts for notes/labels

  * Looking at `allelefreq.png`. Does it make sense to notate the half generations like that? Alleles are only turning over every generation.

7. time to fixation histogram for starting allele freq of 0.5 and pop size of 100 with at least 1000 independent runs

  * were the parameters for the `GentilFixation.png` plot allele freq of 0.5 and pop size of 100? Since you used `sys.argv` for the inputs (which is fine/great), I can't really tell what the parameters were. In such cases, maybe label the plots

8. line plot for fixation time (y-axis) vs N (x-axis) for a starting allele frequency of 0.5 and varied population size (at least 6 different from 100 - 10mil). Label ticks

  * why did you increase the number of simulations as the population size increased? You could have done a single simulation for each population size, but if you were going to do multiple for each different population size, I would have used the same number

9. step 5 running the simulation for a range of 10 starting allele frequencies from 0 to 1. 100 simulations each

10. step 5 plot for variability in the time to fixation for each starting allele frequency. label the ticks and notate population size (0.5 pts for notes and labels)

  * great plot!

Possible bonus points

1. Introduce selection in the simulation function

2. plot the allele frequency trajectory, notating selection coefficient, etc.

3. plot selection coefficient vs time to fixation for fixed population size, note population size on plot
