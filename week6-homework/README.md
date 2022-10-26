 # qbb 2022 Lab 6
 
 # Question 1:
 
 #approx. 37% are valid interactions (average between dCTCF and ddCTCF)
 #Dangling end pairs; this means that the fragments are unligated
 
 python load_data.py analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed heatmap.png
 
 python load_data1.py matrix/dCTCF_full.6400.matrix matrix/ddCTCF_full.6400.matrix matrix/6400_bins.bed heatmap.png
 
 # Question 2:
 
 # The highlighted difference is visable in the full data plot, but not the subsampled plot.
 # With increased sequencing depth, this resolves some of the noise and strengthens real interactions, showing the highlighted region that was not shown before.
 # The highlighed signal indicates a DNA interaction that occurs in the ddCTCF that does not occur in dCTCF.
 
 