#!/usr/bin/env python
# coding: utf-8

import sys
import numpy as np
import pandas as pd
from itertools import combinations_with_replacement

# user input
clear_output = True
ftype = "roses"
haved = ["RRyyWWSs", "rrYYWWss", "rryyWwss"]

# hard coding colors
if ftype == "tulips":
    phenotypes = np.array(["White","White","White","Yellow","Yellow","White","Yellow","Yellow","Yellow","Red","Pink","White","Orange","Yellow","Yellow","Orange","Yellow","Yellow","Black","Red","Red","Black","Red","Red","Purple","Purple","Purple"])[::-1]
elif ftype == "windflowers":
    phenotypes = ["Pink","Pink","Purple","Red","Red","Purple","Red","Red","Purple","Orange","Orange","Orange","Pink","Pink","Pink","Red","Red","Blue","Orange","Orange","Orange","Orange","Orange","Blue","White","White","Blue"]
elif ftype == "mums":
    phenotypes = ["Green","Green","Red","Purple","Purple","Red","Red","Red","Red","Purple","Purple","Purple","Yellow","Red","Pink","Pink","Pink","Pink","Yellow","Yellow","Yellow","Yellow","Yellow","White","White","White","Purple"]
elif ftype == "hyacinths":
    phenotypes = ["Purple","Purple","Purple","Blue","Red","Red","Red","Red","Red","Orange","Yellow","Yellow","Orange","Yellow","Yellow","Red","Pink","White","Yellow","Yellow","Yellow","Yellow","Yellow","White","White","White","Blue"]
elif ftype == "pansies":
    phenotypes = ["Orange","Orange","Purple","Red","Red","Purple","Red","Red","Purple","Yellow","Yellow","Yellow","Orange","Orange","Orange","Red","Red","Blue","Yellow","Yellow","Yellow","Yellow","Yellow","Blue","White","White","Blue"]
elif ftype == "lilies":
    phenotypes = np.array(["White","White","White","Yellow","White","White","Yellow","Yellow","White","Red","Pink","White","Orange","Yellow","Yellow","Orange","Yellow","Yellow","Black","Red","Pink","Black","Red","Pink","Orange","Orange","White"])[::-1]
elif ftype == "cosmos":
    phenotypes = np.array(["White","White","White","Yellow","Yellow","White","Yellow","Yellow","Yellow","Pink","Pink","Pink","Orange","Orange","Pink","Orange","Orange","Orange","Red","Red","Red","Orange","Orange","Red","Black","Black","Red"])[::-1]
elif ftype == "roses":
    phenotypes = ["Yellow","Orange","Orange","Yellow","Orange","Orange","White","Red","Blue","Yellow","Orange","Orange","White","Red","Red","Purple","Red","Black","Pink","Red","Black","Pink","Red","Black","Pink","Red","Black","Yellow","Yellow","Orange","Yellow","Yellow","Orange","White","Pink","Red","Yellow","Yellow","Orange","White","Pink","Red","Purple","Pink","Red","White","Pink","Red","White","Pink","Red","Purple","Pink","Red","Yellow","Yellow","Yellow","Yellow","Yellow","Yellow","White","White","White","Yellow","Yellow","Yellow","White","White","White","Purple","Purple","Purple","White","White","White","White","White","White","Purple","Purple","Purple"]


genotypes_symbol = []
for i in ["RR", "Rr", "rr"]:
    for j in ["YY", "Yy", "yy"]:
        for k in ["WW", "Ww", "ww"]:
            if ftype == "roses":
                for l in ["SS", "Ss", "ss"]:
                    genotypes_symbol.append("%s%s%s%s" % (i,j,k,l))
            else:
                genotypes_symbol.append("%s%s%s" % (i,j,k))

genotypes = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            if ftype == "roses":
                for l in range(3):
                    genotypes.append("%s%s%s%s" % (i,j,k,l))
            else:
                genotypes.append("%s%s%s" % (i,j,k))

g2p = {}
for i,j in zip(genotypes, phenotypes):
    g2p[i] = j

g2gs = {}
gs2g = {}
for i,j in zip(genotypes, genotypes_symbol):
    g2gs[i] = j
    gs2g[j] = i


def single_gene_crossing(gene_combo):
    if gene_combo == "00":
        gene_combo_pool = ["0"]
    elif gene_combo == "11":
        gene_combo_pool = ["0", "1", "2"]
    elif gene_combo == "22":
        gene_combo_pool = ["2"]
    elif gene_combo == "02" or gene_combo == "20":
        gene_combo_pool = ["1"]
    elif gene_combo == "01" or gene_combo == "10":
        gene_combo_pool = ["0", "1"]
    elif gene_combo == "12" or gene_combo == "21":
        gene_combo_pool = ["1", "2"]
    return(gene_combo_pool)


def crossing(f1, f2):
    f1 = gs2g[f1]
    f2 = gs2g[f2]
    pool1 = single_gene_crossing(f1[0]+f2[0])
    pool2 = single_gene_crossing(f1[1]+f2[1])
    pool3 = single_gene_crossing(f1[2]+f2[2])
    if len(f1) == 4:
        pool4 = single_gene_crossing(f1[3]+f2[3])
    
    outcome = []
    for i in pool1:
        for j in pool2:
            for k in pool3:
                if ftype == "roses":
                    for l in pool4:
                        outcome.append("%s%s%s%s" % (i,j,k,l))
                else:
                    outcome.append("%s%s%s" % (i,j,k))
    color = [g2p[f1], g2p[f2]]
    genotype = [g2gs[f1], g2gs[f2]]
    for i in outcome:
        color.append(g2p[i])
        genotype.append(g2gs[i])
    return(pd.DataFrame([genotype, color]))


comb = combinations_with_replacement(haved, 2)
results = []
for pair in comb:
    results.append(crossing(pair[0], pair[1]))

# sort results
# all genotype not haved will be in the front
# the color with less genotypes will be in the front
final_combo = pd.concat(results).iloc[:,[0,1]]

sorted_results = []
for df_result in results:
    result = df_result.T.iloc[2:,:].copy()
    result.columns = ["0", "1"]
    result["haved"] = result["0"].isin(haved)
    result = result.assign(freq=result.groupby('1')['1'].transform('count')).sort_values(by=["freq", "1", "haved"],ascending=[True, True, True])    
    result = result.iloc[:,[0,1]].T
    result.columns = range(result.shape[1])
    sorted_results.append(result)
final = pd.concat(sorted_results)

if clear_output:
    final[final.isin(haved)] = ""

df = pd.concat([final_combo.reset_index(drop=True).T, final.reset_index(drop=True).T]).T

df.to_csv("./%s.tsv" % ftype, sep="\t", header=False, index=False)