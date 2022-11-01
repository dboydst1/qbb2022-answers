 # qbb 2022 week 8
 
 # Part 1
 
 medaka_variant -i methylation.bam -f hg38.fa -r "chr11:1900000-2800000" -o chr11 -p chr11_phased.vcf
 
 medaka_variant -i methylation.bam -f hg38.fa -r "chr14:100700000-100990000" -o chr14 -p chr14_phased.vcf
 
 medaka_variant -i methylation.bam -f hg38.fa -r "chr15:23600000-25900000" -o chr15 -p chr15_phased.vcf
 
 medaka_variant -i methylation.bam -f hg38.fa -r "chr20:58800000-58912000" -o chr20 -p chr20_phased.vcf
 
 # Part 2
 
 whatshap haplotag -o chr11_phased.bam -r ../hg38.fa --regions "chr11:1900000:2800000" --output-haplotag-list chr11_haplotag.txt round_0_hap_mixed_phased.vcf.gz methylation.bam
 
 whatshap haplotag -o chr14_phased.bam -r ../hg38.fa --regions "chr14:100700000:100990000" --output-haplotag-list chr14_haplotag.txt round_0_hap_mixed_phased.vcf.gz methylation.bam
 
 whatshap haplotag -o chr15_phased.bam -r ../hg38.fa --regions "chr15:23600000:25900000" --output-haplotag-list chr15_haplotag.txt round_0_hap_mixed_phased.vcf.gz methylation.bam
 
 whatshap haplotag -o chr20_phased.bam -r ../hg38.fa --regions "chr20:58800000:58912000" --output-haplotag-list chr20_haplotag.txt round_0_hap_mixed_phased.vcf.gz methylation.bam
 
 # Part 3
 
 whatshap split --output-h1 chr11_hap1.bam --output-h2 chr11_hap2.bam chr11_phased.bam chr11_haplotag.txt
 
 whatshap split --output-h1 chr14_hap1.bam --output-h2 chr14_hap2.bam chr14_phased.bam chr14_haplotag.txt
 
 whatshap split --output-h1 chr15_hap1.bam --output-h2 chr15_hap2.bam chr15_phased.bam chr15_haplotag.txt
 
 whatshap split --output-h1 chr20_hap1.bam --output-h2 chr20_hap2.bam chr20_phased.bam chr20_haplotag.txt
 
 samtools cat ./chr11/chr11_hap1.bam ./chr14/chr14_hap1.bam ./chr15/chr15_hap1.bam ./chr20/chr20_hap1.bam > H1_all.bam
 
 samtools cat ./chr11/chr11_hap2.bam ./chr14/chr14_hap2.bam ./chr15/chr15_hap2.bam ./chr20/chr20_hap2.bam > H2_all.bam
 
 samtools index H1_all.bam
 
 samtools index H2_all.bam
 
 # Part 6
 
 # Do you expect each region in H1 or H2 to correspond to the same parent of origin (i.e. the same haplotype)? Explain your reasoning.
 
 #H1 matches for female on chr11 (high methylation), chr14 (low methylation), chr 15 (high methylation), but not for chr 20 (shows high methylation followed by low methylation).
 #H2 shows the opposite phenotype for all loci.
 
 # I do not expect each region in H1 or H2 to correspond to the same parent of origin, because the haplotype shown for chr 20 shows the opposite differential methylation than the other three loci in chr 11, 14, and 15 for both haplotypes.