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
 
 