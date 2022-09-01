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
 
 #Exercise 3
 
 #Synopsis: This bash function (do_all.sh) will take a vcf and gtf file, parse through the information, and output a histogram showing the allele counts for differing gene types. This is useful for comparing the trends of allele counts for different gene types.
 
 #Usage: bash do_all.sh [file.vcf] [file.gtf]
 
 #Dependencies: requires bedtools and matplotlib
 
 #Description: 
 # 1. Loads VCF and GTF files
 # 2. Creates .bed files for features of interest
 # 		--Runs subset_regions.sh on the GTF file
 #			--bash script
 #			--uses grep to separate out a specfific chromosome and save it in a gtf file
 #			--searches through protein types and makes a bed file for them
 #			--finds Exons and makes a bed file for it
 # 3. Subsets a .vcf for each feature
 #		--
 # 4. Plots Allele Count histogram for each .vcf
 #		--Runs plot_vcf_ac.py to plot each .vcf
 
 
 #Output
 
 