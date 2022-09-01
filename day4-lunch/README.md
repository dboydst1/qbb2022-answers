 # qbb2022 lunch exercises
 
 #Exercise 1
 
 #--- Subsetting exons.chr21.bed.vcf
 #    + Covering 1107407 bp
 #--- Subsetting processed_pseudogene.chr21.bed.vcf
 #    + Covering 956640 bp
 #--- Subsetting protein_coding.chr21.bed.vcf
 #    + Covering 13780687 bp
 
 #one strategy to confirm if they are identical is by running the bash code:
 cmp -b exons.chr21.bed.vcf.png cache/exons.chr21.bed.vcf.png
 
 #performing this command shows they are different in byte 73, line 3.
 
 #lncRNA, processed_pseudogene, and snRNA are all interesting to find within a gene
 
 
 #Exercise 2
 
 #The graphs are all very skewed to the left, with processed pseudogenes having a slight uptick toward the center of the x.
 
 