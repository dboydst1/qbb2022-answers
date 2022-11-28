#usr/bin/env python
import pandas as pd
import scanpy as sc
from matplotlib.pyplot import rc_context
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.tl.pca(adata)
sc.pl.pca(adata, title = 'PCA of prefiltered Data', save = 'prefilterPCA.png')

sc.pp.recipe_zheng17(adata)
sc.tl.pca(adata)
sc.pl.pca(adata, title = 'PCA of Filtered Data', save = 'filteredPCA.png')

sc.pp.neighbors(adata)
sc.tl.leiden(adata, key_added='clusters')
# for thing in adata.var.index:
#     print(thing)

sc.tl.tsne(adata)
sc.pl.tsne(adata, title = 'tSNE of Clusters', color = 'clusters', save = 'tSNE.png')

sc.tl.umap(adata, maxiter = 1000)
sc.pl.umap(adata, title = 'UMAP of Clusters', color = 'clusters', save = 'UMAP.png')

sc.tl.rank_genes_groups(adata, 'clusters', method='t-test')
sc.pl.rank_genes_groups(adata, save = 'ttest.png')

sc.tl.rank_genes_groups(adata, 'clusters', method = 'logreg')
sc.pl.rank_genes_groups(adata, save = 'logreg.png')

marker_type = ['Schwann Cells', 'Oligodendrocytes', 'Astrocytes', 'Microglia', 'GABAergic Neurons', 'EC type 3']
marker_genes = ['Gap43', 'Olig2', 'Aldh1l1', 'Cd68', 'Adora2a', 'Alas2']

sc.tl.tsne(adata)
sc.pl.tsne(adata, color = marker_genes, save = 'markergenes.png')

marker_genes_dict = {
    'Schwann Cells': ['Gap43'],
    'Oligodendrocytes': ['Olig2'],
    'Astrocytes': ['Aldh1l1'],
    'Microglia': ['Cd68'],
    'GABAergic Neurons': ['Adora2a'],
    'EC type 3': ['Alas2'],
}

cluster2annotation = {
     '0': '0',
     '1': '1',
     '2': '2',
     '3': '3',
     '4': '4',
     '5': 'Astrocytes',
     '6': '6',
     '7': '7',
     '8': '8',
     '9': '9',
     '10': '10',
     '11': '11',
     '12': '12',
     '13': '13',
     '14': '14',
     '15': '15',
     '16': 'EC type 3',
     '17': '17',
     '18': '18',
     '19': '19',
     '20': '20',
     '21': 'Oligodendrocytes',
     '22': '22',
     '23': 'GABAergic Neurons',
     '24': 'Schwann Cells',
     '25': '25',
     '26': 'Microglia',
     '27': '27',
     '28': '28',
}

adata.obs['cell type'] = adata.obs['clusters'].map(cluster2annotation).astype('category')
sc.tl.tsne(adata)
sc.pl.tsne(adata, color='cell type', legend_loc='on data', save = 'tSNEFinal.png')