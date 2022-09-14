 # qbb 2022 Week 1 Assignment, Darren Boydston
 
 # Question 1.1
 # 1Mbp * 5 = 5Mbp; 5Mbp / 100 bp = 50,000
 # 1Mbp * 15 = 15Mbp; 15Mbp / 100 bp = 150,000
 
 # Question 1.3
 # In my randomly generated run, 6617 bases had 0x coverage. The poisson distribution predicts 6808 bases to have 0x coverage. In this case, the actual coverage was slightly better than what the poisson distribution predicts.
 
 # Question 1.4
 # In this run, the genome had 25 bases with 0x coverage, where the poisson distribution predicted no bases with 0x coverage. In this case, the actual coverage was slightly worse than what the poisson distribution predicts.
 
 ~/miniconda3/bin/SPAdes-3.15.5-Darwin/bin/spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31
 
 # Question 2.1
 # There are 4 contigs
 
 grep -c '>' contigs.fasta
 
 # Question 2.2
 # length 105830 + 47860 + 41351 + 39426 = 234,497 bp
 
 less -S contigs.fasta
 
 # Question 2.3
 # length 105830 bp
 
 # Question 2.4
 # N50 = 47860 bp

 dnadiff ref.fa scafforlds.fasta
 less -S out.report
 
 # Question 3.1
 # Avg identity of ref and assembly is 99.98
 
 show-coords out.delta
 
 # Question 3.2
 # Longest length is 20700
 
 less -S out.report
 
 # Question 3.3
 # There is one insertion and no deletions
 
 # Question 4.1
 # The position of insertion is at 26787 - 27498
 
 # Question 4.2
 # The novel insertion is 712 bp long
 
 samtools faidx scaffolds.fasta NODE_1_length_234497_cov_20.506978:26788-27498
 
 # Question 4.3 #CATACAATGCGTATTGTAGTATGGCCTTACGGGAGGGCAGACGGCAAAGAGTGATCACGTTCTATCGGATGCAAGGCACCGCTTTATCCATTAGCCTCTTATTGGAGGAGGGCATGGCATTCATACCCAATGGCTCAATTCTTTTACTACAACATTGATAACTTATCCAAGTACTCTACGACCAACCTGCAGAACGGCCCACCGGCCTAACGGCATACCTCACAACTACCCTGCTAAGGCGAGCACTCCAGCCAAGCAAGACCACATCCACCCAAGCCCACCTCATCGCCTCAGCCAATAGCGCTCAGACAAAAGGAACTTATTATTAACTGAAACGCTGTACTGCGGTAAGTCCTCAACGCCGACCAAACGAAACCAGCAGCGTAGTCCTATCGGACTCGCTTGCACACATAACACATGCTTGTAGTCTTGCACGACCCCAGGCGGACATGAGTTTCTGCTGGGCGGCGAGGAGTCGAAGCTGCGGGCATTCCTTTCCGAAAACATGAATTACTGCGGGTATGTCCGACCTCAAACATTCGTACCTGAGCATATTGCTCAAGTGAGCCAGTCGGCAATTCATATCCGAAAACATGACTGTCTTGCATAAGGCCTCTCTTACGAGCTGAGTGCACGAACCACGGAACAGCTTAGTCACTTAGAAGAGTACTCTATTCGGGACTTGAAGTACGCGTGCAATCGGGAACTAGTG
 
 # Question 4.4
 
 ../dna-decode.py --decode --input secret.fasta
 
 # Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens..
 
 