 # QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn to code.
 
 wc exons.chr21.bed #13653 lines
 wc genes.chr21.bed #219 lines
 
 #62.34 Exons per Gene
 
 #to find the median, I would find the number of exons per gene by "counting" the number of exons in each gene region, then sort for the middle value of all the counts of exons per gene.
 
 cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq -c
 #305 1
 #17 10
 #17 11
 #30 12
 #62 13
 #228 14
 #992 15
 #678 2
 #79 3
 #377 4
 #808 5
 #148 6
 #1050 7
 #156 8
 #654 9
 
 #I would subtract the start of the site by the end of the site for every region, then I would sort these absolute sizes by region, and add each region indepentently. Whatever number is largest would take up the most amount of space in the genome.
 
sort -k 2 integrated_call_samples.panel | cut -f 2,3 | uniq -c | grep AFR

 #123 ACB	AFR
 #112 ASW	AFR
 #173 ESN	AFR
 #180 GWD	AFR
 #122 LWK	AFR
 #128 MSL	AFR
 #206 YRI	AFR

 #I would use the same function, but change AFR to the name of the other groups