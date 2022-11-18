#usr/bin/env python

import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.tl.pca(adata)
# sc.pl.pca(adata, title = 'PCA of prefiltered Data', save = 'prefilterPCA.png')

sc.pp.recipe_zheng17(adata)
sc.tl.pca(adata)
# sc.pl.pca(adata, title = 'PCA of Filtered Data', save = 'filteredPCA.png')

sc.pp.neighbors(adata)
sc.tl.leiden(adata)
for thing in adata.var.index:
    print(thing)

# sc.tl.tsne(adata)
# sc.pl.tsne(adata, title = 'tSNE of Clusters', color = 'leiden', save = 'tSNE.png')
#
# sc.tl.umap(adata, maxiter = 1000)
# sc.pl.umap(adata, title = 'UMAP of Clusters', color = 'leiden', save = 'UMAP.png')
#
# sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
# sc.pl.rank_genes_groups(adata, save = 'ttest.png')
#
# sc.tl.rank_genes_groups(adata, 'leiden', method = 'logreg')
# sc.pl.rank_genes_groups(adata, save = 'logreg.png')

marker_type = ['Microglia', 'Oligodendrocytes', 'Astrocytes', 'EC1', 'EC2', 'EC3']
marker_genes = ['F13a1', 'Tmem132b', 'P4ha3', 'F5', 'Ctsw', 'Alas2']

sc.tl.tsne(adata)
sc.pl.tsne(adata, color = marker_genes, save = 'markergenes.png')