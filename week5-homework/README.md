 # qbb week 5 homework
 
 samtools view D2_Sox2_R1.bam -q 10 -b > D2_Sox2_R1_filtered.bam
 samtools view D2_Sox2_R2.bam -q 10 -b > D2_Sox2_R2_filtered.bam
 samtools view D2_Sox2_R1_input.bam -q 10 -b > D2_Sox2_R1_input_filtered.bam
 samtools view D2_Sox2_R2_input.bam -q 10 -b > D2_Sox2_R2_input_filtered.bam
 
 macs2 callpeak -t D2_Sox2_R1_filtered.bam -c D2_Sox2_R1_input_filtered.bam -B -g 94987271
 macs2 callpeak -t D2_Sox2_R2_filtered.bam -c D2_Sox2_R2_input_filtered.bam -B -g 94987271
 
 bedtools intersect -a R1_directory/NA_peaks.narrowPeak -b R2_directory/NA_peaks.narrowPeak > Sox2Intersect.bed
 
 bedtools intersect -a D2_Klf4_peaks.bed -b Sox2Intersect.bed > Klf4Sox2Peaks.bed
 
 wc -l Klf4Sox2Peaks.bed
 #40
 wc -l D2_Klf4_peaks.bed
 #60
 
 # 40/60 = 66.67%
 
 python scale_bdg.py /R1_directory/NA_treat_pileup.bdg ????