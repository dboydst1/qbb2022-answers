# Week 1 Genome Assembly -- Feedback

1 + 1 + 1 + 1 + 1 + 1 + 0.75 + 0.825 + 0.5 + 0.5 = 8.58 points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * --> +1

2. Question 1.2, 1.4 simulation script(s)

  * great simulation! Consider using a single script that accepts command line/user input or a function that you can pass generalized variables to rather than having repetitive code --> +1

3. Question 1.2, 1.4 plotting script(s)

  * your method for plotting the Poisson distribution works, but rather than simulating from a Poisson distribution, you can find exact expectations by using the probability mass function, something like the example 2 in the following next time: https://www.geeksforgeeks.org/how-to-create-a-poisson-probability-mass-function-plot-in-python/

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * Interesting plots! You should add a legend that says which is observed and which is expected. Alternatively, you could do a line plot for the expected and keep the histogram for the observed --> +1

5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * good work, but again the PMF poisson approach can give more exact/precise results --> +1

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * # of contigs --> +0.5
  * total length of contigs --> +0.5

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.5
  * contig n50 size, --> +0.25, please explain your reasoning

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> there should be some deletions, + 0.33/2

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> +0.25, which position do you think and how did you get this?
  * length of novel insertion --> +0.25, how did you get this?

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +0.25
  * secret message --> +0.25

  you don't provide a consistent position for the insertion in the final two answers (`samtools faidx` uses a different position than you provide for 4.1), and the provided DNA sequence would not produce the correct output message. If you remove the first DNA base, however it does. We're okay with you working with other people, but we want to make sure that you also understand the commands that you're running. If your code isn't working, you're always welcome to reach out for help, either from classmates or from the TAs. So, if you really did get the correct output, please correct the commands you used, but if you were having trouble getting that output, let us know and we can help.
