Really great job! There is one issue that's going to disrupt your regression results:
1. When you're grabbing the pvals and betas from the regression, it looks like you're doing `results.pvalues[0]`, but I think that may be grabbing the pvalue for the intercept, NOT the slope of the regression line. So you're essentially testing whether the transcripts are expressed at all or not, and given that we already filtered the transcripts, most of them will probably have a significant intercept. You should be able to choose specifically which pval and beta you want using the names of the factors (something like `results.pvalues['stage']`). This is affecting your gene lists and volcano plot, but the rest of your code looks like it's correct (-0.5 point)

Excellent job overall.
(9.5/10)
