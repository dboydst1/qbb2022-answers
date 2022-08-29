 #GBB2022 - Day 1 - Homework Exercises Submission
 
 #Exercise 1
 
 #We see an awk: Illegal Field $() error
 #This can be fixed by defining nuc=$nuc within the awk -v command
 
 #!/bin/bash

 #USAGE: bash exercise1.sh input_VCF

 for nuc in A C G T
 do
   echo "Considering" $nuc
   awk -v nuc=$nuc '/^#/{next} {if ($4 == nuc) {print $5}}' $1 | sort | uniq -c
 done
 
 
 #Output:
 #Considering A
 #354 C
 #1315 G
 #358 T
 #Considering C
 #484 A
 #384 G
 #2113 T
 #Considering G
 #2041 A
 #405 C
 #485 T
 #Considering T
 #358 A
 #1317 C
 #386 G

 #These results make biological sense, because we should see that alternate SNPS should be changing to a different pair, and are more likely to accept one from a pair in that position than the other of the pair.
 
 #Exercise 2
 
 grep -Ew "1|2|10|11" chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > chrom121011.bed #this command subsets all promoters from the reference file.
 
 bedtools intersect -a random_snippet.vcf -b chrom121011.bed | grep -v "#" | awk '{if ($4 == "C") {print $5}}' | sort | uniq -c #This command finds the alternate alleles
 
 #output:
 #12 A
 #11 G
 #39 T
 
 #T seems to be a preferred SNP within promoter regions
 
 #Exercise 3
 
 #!/bin/bash

 #USAGE: bash exercise3.sh input_VCF

 awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed #This command removes anything starting with a # and prints out a bed file with the necessary columns of info
 sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed #This line is sorting the columns in the gene bed file
 bedtools closest -a variants.bed -b genes.sorted.bed #This line determines the closest match between the variants and genes
 
 awk '/^#/{next} BEGIN{OFS="\t"} {print $1,$2-1, $2}' $1 > variants.bed #SET as tab delimited
 sort -k1,1 -k2,2n variants.bed > variants.sorted.bed #Sort variants file
 sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
 bedtools closest -a variants.sorted.bed -b genes.sorted.bed
 
 bedtools closest -a variants.sorted.bed -b genes.sorted.bed | wc -l
 #There are 10293 variants
 
 bedtools closest -a variants.sorted.bed -b genes.sorted.bed | cut -f 7 | sort | uniq | wc -l
 #There are 200 genes
 
 #There are 51.465 variants per genes
 
 #Exersise 4
 
 bedtools intersect -a H3K27ac.naive_b_cell.GRCh38.bedgraph -b genes.bed -wb | cut -f 8 | sort | uniq > genes_intersecting_H3K27ac_b_cell.txt #This line finds the intersections of H3K27ac and genes, it cuts out the column showing the gene name, sorts it, then determines how many uniqe genes there are, and finally saves it to a file

 bedtools intersect -a H3K9me3.naive_b_cell.GRCh38.bedgraph -b genes.bed -wb | cut -f 8 | sort | uniq > genes_intersecting_H3K9me3_b_cell.txt #This file does the same thing as the last one, but with the H3K9me3 file

 grep -v -f genes_intersecting_H3K27ac_b_cell.txt genes_intersecting_H3K9me3_b_cell.txt #This line identifies the overlaps? this line doesn't make a lot of sense to me.
 
 #!/bin/bash

 #USAGE: bash exercise4.sh

 #Goal: report any genes that uniquely intersect with H3K27ac but never intersect with H3K9me3 within naive B cells.

 bedtools intersect -a H3K27ac.naive_b_cell.GRCh38.bedgraph -b genes.bed -wb | cut -f 8 | sort | uniq > genes_intersecting_H3K27ac_b_cell.txt

 bedtools intersect -a H3K9me3.naive_b_cell.GRCh38.bedgraph -b genes.bed -wb | cut -f 8 | sort | uniq > genes_intersecting_H3K9me3_b_cell.txt

 grep -v -f genes_intersecting_H3K9me3_b_cell.txt genes_intersecting_H3K27ac_b_cell.txt #The logic error was in the file order here.
 
 #the syntax error was in the file directory. this was corrected by copying the files to the working directory.
 
 #The output was CRYAA
 
 #Exercise 5
 
 
 
 
 
 
 
 