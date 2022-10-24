# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 1 + 0.75 + 1 + 1 + 1 + 1 + 1 = 9.75 points out of 10 possible points

1. Index genome

  * --> +1

2. align reads

  * --> +1 ; fantastic

3. sort bam files and index sorted bam files (0.5 points each)

  * --> +1; very good, but consider using a single for loop for questions 2 & 3

4. variant call with freebayes

  * want to use the `-p` argument to specify the ploidy of the yeast (1)
  * --> +0.75

5. filter variants

  * --> +1

6. decompose complex haplotypes

  * --> +1

7. variant effect prediction

  * --> +1

8. python plotting script

  * very cool use of the `allel` package and its `read_vcf`!!
  * nice list comprehension, but I didn't realize the data had NaN's. I wonder if the `allel` function translates the `.` to NaN's by default.
  * did you need/use `enumerate()` and the i indices with your `for` loops? You could simplify them algorithmically to just be `for each in callset['calldata/GQ']` for example. You also can use a nested for loop for your annotation effect list.  

9. 4 panel plot (0.25 points each panel)

  * the labels, titles etc aren't readable in your plot. Try a `plt.tight_layout()` or adjusting the figure size

10. 1000 line vcf

  * --> +1
