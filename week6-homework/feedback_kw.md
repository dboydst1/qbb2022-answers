## Week 6 -- 10 points possible

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 13 of 10 points possible

1. Given data question: What percentage of reads are valid interactions?

2. Given data question: What constitutes the majority of invalid 3C pairs?/What does it mean?

3. Script set up to (0.5 pts each)

  * read in data  
  * Filter data based on location  
    * you can use a simpler approach/boolean indexing to do this without a for loop, like the following:

    ```
    data1 = data1[numpy.where((data1['F1'] >= start_bin) &
                                  (data1['F2'] < end_bin))]
    ```

4. Script set up to log transform the scores
  * again you can do this more simply without a `for` loop, like the following. `data1['score'] = numpy.log(data1['score'])`. It applies the log to all the scores in the array/along the axis.


5. Script set up to shift the data by subtracting  minimum value
  * You can find the minimum without a for loop:
  `minimum1 = np.amin(data1['score'])`. It finds the minimum value in the whole array.
  * then you can subtract the minimum without a `for` loop: `data1['score'] -= minimum1`. It subtracts the minimum value from each of the scores in the array

6. Script set up to convert sparse data into square matrix
  * what you have again works like all the other for loops, but you can do something without a for loop: `mat[data1["F1"] - start_bin, data1["F2"] - start_bin] = data1['score']` and this will fill in the whole `mat` array for each combo/row of F1, F2, and score values

7. Script set up to (0.33 pts each)

  * remove distance dependent signal
  * smooth
  * subtract

8. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for subset dataset (0.33 pts each ddCTCF/dCTCF/difference)

9. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for full dataset (0.33 pts each ddCTCF/dCTCF/difference)

10. Heatmap questions (0.33 pts each)

  * See the highlighted difference from the original figure?
  * impact of sequencing depth?
  * highlighted signal indicates?

Possible Bonus points:

1. Insulation script set up to (0.25 pts each)

  * read in data
  * filter data based on location
  * log transform the data
  * shift the data by subtracting minimum value

2. Insulation script set up to (0.5 pts each)

  * convert sparse data into square matrix
  * find the insulation score by taking mean of 5x5 squares of interactions around target

3. Turned in the plot of the heatmap + insulation scores below (0.5 pts each panel)

  * insulation scores below should be a line plot with location being the x-axis point and insulation score being the y-axis point. This was not clear in the assignment write up though. Sorry.
