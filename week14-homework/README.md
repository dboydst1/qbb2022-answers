# qbb week 14 answers
 
 #Step 1B, I used the sample code
 
python conversioncode.py metagenomics_data/step0_givendata/KRAKEN/SRR492183.kraken SRR492183
python conversioncode.py metagenomics_data/step0_givendata/KRAKEN/SRR492186.kraken SRR492186
python conversioncode.py metagenomics_data/step0_givendata/KRAKEN/SRR492188.kraken SRR492188
python conversioncode.py metagenomics_data/step0_givendata/KRAKEN/SRR492189.kraken SRR492189
python conversioncode.py metagenomics_data/step0_givendata/KRAKEN/SRR492190.kraken SRR492190
python conversioncode.py metagenomics_data/step0_givendata/KRAKEN/SRR492193.kraken SRR492193
python conversioncode.py metagenomics_data/step0_givendata/KRAKEN/SRR492194.kraken SRR492194
python conversioncode.py metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197

ktImportText -q SRR492183_krona.txt
ktImportText -q SRR492186_krona.txt
ktImportText -q SRR492188_krona.txt
ktImportText -q SRR492189_krona.txt
ktImportText -q SRR492190_krona.txt
ktImportText -q SRR492193_krona.txt
ktImportText -q SRR492194_krona.txt
ktImportText -q SRR492197_krona.txt

# Question 1

 #On the first day, ("snapshot.svg") diversity is surprisingly high, with high Staph. epidermis, Enterococcus faecalis, and cutibacterium avidum. Diversity quickly drops off in the second day ("snapshot-2.svg"), with Enterococcus faecalis making up 91% of the sample. From this time onward, diversity slowly increases again, and Enterococcus faecalis drops to 60%. Viral presence increases, and actinobacteria increase to ~27-28%.
 
# Question 2

 # We could potentially use things like compare read counts of different contigs (contigs from the same species should have similar coverage), or characteristics of the contigs, like GC content, codon usage, or known genes on the contigs.
 
bwa index metagenomics_data/step0_givendata/assembly.fasta
bwa mem -t 4 -o SRR492183.sam assembly.fasta READS/SRR492183_1.fastq READS/SRR492183_2.fastq
bwa mem -t 4 -o SRR492186.sam assembly.fasta READS/SRR492186_1.fastq READS/SRR492186_2.fastq
bwa mem -t 4 -o SRR492188.sam assembly.fasta READS/SRR492188_1.fastq READS/SRR492188_2.fastq
bwa mem -t 4 -o SRR492189.sam assembly.fasta READS/SRR492189_1.fastq READS/SRR492189_2.fastq
bwa mem -t 4 -o SRR492190.sam assembly.fasta READS/SRR492190_1.fastq READS/SRR492190_2.fastq
bwa mem -t 4 -o SRR492193.sam assembly.fasta READS/SRR492193_1.fastq READS/SRR492193_2.fastq
bwa mem -t 4 -o SRR492194.sam assembly.fasta READS/SRR492194_1.fastq READS/SRR492194_2.fastq
bwa mem -t 4 -o SRR492197.sam assembly.fasta READS/SRR492197_1.fastq READS/SRR492197_2.fastq

samtools sort -O bam -o SRR492183.bam SRR492183.sam
samtools sort -O bam -o SRR492186.bam SRR492186.sam
samtools sort -O bam -o SRR492188.bam SRR492188.sam
samtools sort -O bam -o SRR492189.bam SRR492189.sam
samtools sort -O bam -o SRR492190.bam SRR492190.sam
samtools sort -O bam -o SRR492193.bam SRR492193.sam
samtools sort -O bam -o SRR492194.bam SRR492194.sam
samtools sort -O bam -o SRR492197.bam SRR492197.sam

cp ~/miniconda3/envs/metabat2/lib/libdeflate.so ~/miniconda3/envs/metabat2/lib/libdeflate.0.dylib
conda activate metabat2

jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam
metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin

# Question 3
 #A. 6 Bins
 
grep -v ">" assembly.fasta | wc -m
 #38708237
grep -v ">" bins_dir/bin.*.fa | wc -m
 #17365118
 #B. 17365118/38708237 = 44.86%

grep -v ">" bins_dir/bin.1.fa | wc -m
 #2.75 Mb
grep -v ">" bins_dir/bin.2.fa | wc -m
 #2.29 Mb
grep -v ">" bins_dir/bin.3.fa | wc -m
 #1.68 Mb
grep -v ">" bins_dir/bin.4.fa | wc -m
 #1.25 Mb
grep -v ">" bins_dir/bin.5.fa | wc -m
 #2.53 Mb
grep -v ">" bins_dir/bin.6.fa | wc -m
 #2.91 Mb
 
 #C. Most prokaryotic genomes tend to be approx. ~2.5 Mb in size, and almost never larger than 5 Mb. The smallest prokaryotic genome is 1.3 Mb. Bin 4 is most certainly too small, and bin 3 is likely too small.
 
 #D. Estimations can come from approximation of average genome size to smallest/largest known prokaryotic genomes. Additionally, attempting to annotate genes in each bin may provide an idea about how many genes are in each bin, and you can compare this to the smallest/largest number of known genes in a genome. Additionally, mapping these to a reference may tell you that some genes within the same bin are from different phyla, indicating contamination.
 
head bins_dir/bin.*.fa 
grep NODE_12_length_269228_cov_106.168966 KRAKEN/assembly.kraken
grep NODE_20_length_181746_cov_381.691663 KRAKEN/assembly.kraken
grep NODE_3_length_498518_cov_181.760000 KRAKEN/assembly.kraken
grep NODE_14_length_235766_cov_39.967778 KRAKEN/assembly.kraken
grep NODE_4_length_455101_cov_112.371015 KRAKEN/assembly.kraken
grep NODE_1_length_1447137_cov_2268.097092 KRAKEN/assembly.kraken
 
# Question 4
 #A. Bin1 = Staphylococcus aureus subsp. aureus CN1; Bin2 = Staphylococcus epidermidis RP62A; Bin3 = Anaerococcus prevotii DSM 20548; Bin4 = Staphylococcus haemolyticus JCSC1435; Bin5 = Cutibacterium avidum;Cutibacterium avidum 44067; Bin6 = Enterococcus faecalis OG1RF
 #B. A more accurate approach would be to make a phylogenetic tree of the bins in relation to each other, then predict the classification based on the confidence of the phylogenetic analysis.