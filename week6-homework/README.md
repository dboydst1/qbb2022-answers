 # qbb 2022 Lab 6
 
 # Question 1:
 
 #approx. 37% are valid interactions (average between dCTCF and ddCTCF)
 #Dangling end pairs; this means that the fragments are unligated
 
 python load_data.py analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed heatmap.txt
 
 # Question 2:
 
 # I do not see the highlighted difference in my figure (though perhaps this is my own shortfall with the coding).
 # With increased sequencing depth, this resolves some of the noise and strengthens real interactions.
 # If my code is correct, the highlighted signal in the paper is likely just noise, and is not a real difference in interaction.