#!/usr/bin/env python 

"""Usage: ./wk14A.py """

import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")

import scanpy.api as sc
sc.settings.autoshow = False


# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()
#print("after")

sc.tl.pca(adata)
sc.pl.pca(adata, save="unfiltered.png")


filtered = sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=True)

filtered_PCA = sc.tl.pca(filtered)
sc.pl.pca(filtered, save="filtered.png")

sc.pp.neighbors(adata, n_neighbors=15)
sc.tl.louvain(adata, resolution=None)

sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
sc.pl.tsne(adata, color = "louvain", save = ("t_sne"))

sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
sc.pl.umap(adata, color = "louvain", save = ("u_map"))

sc.tl.rank_genes_groups(adata, groupby = "louvain", method='t-test_overestim_var', corr_method='benjamini-hochberg')
sc.pl.rank_genes_groups(adata, save = ("t-test"))

sc.tl.rank_genes_groups(adata, groupby = "louvain", method='logreg')
sc.pl.rank_genes_groups(adata, save = ("log_reg"))

#sc.pl.dotplot(adata, var_names, groupby=None, use_raw=None, log=False, num_categories=7, color_map='Reds', figsize=None, dendrogram=False, var_group_positions=None, var_group_labels=None, var_group_rotation=None, layer=None, show=None, save=None, **kwds)
#sc.pl.clustermap(adata, save=None)
#sc.pp.filter_genes(adata, min_counts=1)  # only consider genes with more than 1 count
#sc.pp.normalize_per_cell(                # normalize with total UMI count per cell
#     adata, key_n_counts='n_counts_all')
#filter_result = sc.pp.filter_genes_dispersion(  # select highly-variable genes
#    adata.X, flavor='cell_ranger', n_top_genes=n_top_genes, log=False)
#adata = adata[:, filter_result.gene_subset]     # subset the genes
#sc.pp.normalize_per_cell(adata)          # renormalize after filtering
#if log: sc.pp.log1p(adata)               # log transform: adata.X = log(adata.X + 1)
#sc.pp.scale(adata)                       # scale to unit variance and shift to zero mean