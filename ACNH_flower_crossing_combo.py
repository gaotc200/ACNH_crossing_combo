#!/usr/bin/env python
# coding: utf-8

import sys
import numpy as np
import pandas as pd
from itertools import combinations_with_replacement

ftype = "tulips"
had = ["rryyWw", "rrYYww", "RRyyWw"]

class flower_crossing():
    def __init__(self, ftype):
        self.ftype = ftype
        
        # all gene combo in symbol
        self.genotypes_symbol = []
        for i in ["RR", "Rr", "rr"]:
            for j in ["YY", "Yy", "yy"]:
                for k in ["WW", "Ww", "ww"]:
                    if ftype == "roses":
                        for l in ["SS", "Ss", "ss"]:
                            self.genotypes_symbol.append("%s%s%s%s" % (i,j,k,l))
                    else:
                        self.genotypes_symbol.append("%s%s%s" % (i,j,k))

        # all gene combo in number
        self.genotypes = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if ftype == "roses":
                        for l in range(3):
                            self.genotypes.append("%s%s%s%s" % (i,j,k,l))
                    else:
                        self.genotypes.append("%s%s%s" % (i,j,k))

        # all correspond colors
        if ftype == "tulips":
            self.phenotypes = np.array(["White","White","White","Yellow","Yellow","White","Yellow","Yellow","Yellow","Red","Pink","White","Orange","Yellow","Yellow","Orange","Yellow","Yellow","Black","Red","Red","Black","Red","Red","Purple","Purple","Purple"])[::-1]
        elif ftype == "windflowers":
            self.phenotypes = ["Pink","Pink","Purple","Red","Red","Purple","Red","Red","Purple","Orange","Orange","Orange","Pink","Pink","Pink","Red","Red","Blue","Orange","Orange","Orange","Orange","Orange","Blue","White","White","Blue"]
        elif ftype == "mums":
            self.phenotypes = ["Green","Green","Red","Purple","Purple","Red","Red","Red","Red","Purple","Purple","Purple","Yellow","Red","Pink","Pink","Pink","Pink","Yellow","Yellow","Yellow","Yellow","Yellow","White","White","White","Purple"]
        elif ftype == "hyacinths":
            self.phenotypes = ["Purple","Purple","Purple","Blue","Red","Red","Red","Red","Red","Orange","Yellow","Yellow","Orange","Yellow","Yellow","Red","Pink","White","Yellow","Yellow","Yellow","Yellow","Yellow","White","White","White","Blue"]
        elif ftype == "pansies":
            self.phenotypes = ["Orange","Orange","Purple","Red","Red","Purple","Red","Red","Purple","Yellow","Yellow","Yellow","Orange","Orange","Orange","Red","Red","Blue","Yellow","Yellow","Yellow","Yellow","Yellow","Blue","White","White","Blue"]
        elif ftype == "lilies":
            self.phenotypes = np.array(["White","White","White","Yellow","White","White","Yellow","Yellow","White","Red","Pink","White","Orange","Yellow","Yellow","Orange","Yellow","Yellow","Black","Red","Pink","Black","Red","Pink","Orange","Orange","White"])[::-1]
        elif ftype == "cosmos":
            self.phenotypes = np.array(["White","White","White","Yellow","Yellow","White","Yellow","Yellow","Yellow","Pink","Pink","Pink","Orange","Orange","Pink","Orange","Orange","Orange","Red","Red","Red","Orange","Orange","Red","Black","Black","Red"])[::-1]
        elif ftype == "roses":
            self.phenotypes = ["Yellow","Orange","Orange","Yellow","Orange","Orange","White","Red","Blue","Yellow","Orange","Orange","White","Red","Red","Purple","Red","Black","Pink","Red","Black","Pink","Red","Black","Pink","Red","Black","Yellow","Yellow","Orange","Yellow","Yellow","Orange","White","Pink","Red","Yellow","Yellow","Orange","White","Pink","Red","Purple","Pink","Red","White","Pink","Red","White","Pink","Red","Purple","Pink","Red","Yellow","Yellow","Yellow","Yellow","Yellow","Yellow","White","White","White","Yellow","Yellow","Yellow","White","White","White","Purple","Purple","Purple","White","White","White","White","White","White","Purple","Purple","Purple"]
        

        self.g2gs = {} # get gene number from gene symbol
        self.gs2g = {} # get gene symbol from gene number
        self.g2p = {} # get color from gene number
        self.gs2p = {} # get color from gene symbol
        for i,j,k in zip(self.genotypes, self.phenotypes, self.genotypes_symbol):
            self.g2p[i] = j
            self.gs2p[k] = j
            self.g2gs[i] = k
            self.gs2g[k] = i
    

    def crossing(self, f1, f2):
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
    
        f1 = self.gs2g[f1]
        f2 = self.gs2g[f2]
        pool1 = single_gene_crossing(f1[0]+f2[0])
        pool2 = single_gene_crossing(f1[1]+f2[1])
        pool3 = single_gene_crossing(f1[2]+f2[2])
        if len(f1) == 4:
            pool4 = single_gene_crossing(f1[3]+f2[3])

        outcome = []
        for i in pool1:
            for j in pool2:
                for k in pool3:
                    if self.ftype == "roses":
                        for l in pool4:
                            outcome.append("%s%s%s%s" % (i,j,k,l))
                    else:
                        outcome.append("%s%s%s" % (i,j,k))
        out_genotype = []
        for i in outcome:
            out_genotype.append(self.g2gs[i])
        return out_genotype

color_dict = {
    "Red":    "#ff5c5c",
    "White":  "#ffeded",
    "Yellow": "#fdff78",
    "Purple": "#7866ff",
    "Pink":   "#ffaea3",
    "Green":  "#00ff2a",
    "Blue":   "#1e00ff",
    "Black":  "#616161",
    "Orange": "#ff8c21"
}

with open("./ACNH_crossing_result.html", "w", encoding='utf8') as htmlf:
    htmlf.write("""<!DOCTYPE html>
<html>
<head>
    <title>ACNH</title>
    <style>
        table, th, td {
            padding: 5px;
        }
        table {
            border-spacing: 5px;
        }
    </style>
</head>
<body>
    <div style="text-align:center">
        <table style="margin:auto">
            <tr>
                <th>P1</th>
                <th>&#215</th>
                <th>P2</th>
                <th>=</th>
                <th>F1</th>
            </tr>
""")

    fl = flower_crossing(ftype)
    comb = combinations_with_replacement(had, 2)
    str1 = []
    str2 = []
    for p1gene,p2gene in comb:
        comb_result = []
        crossing_outcome_genotype = np.array(fl.crossing(p1gene, p2gene))
        crossing_outcome_color = np.array([fl.gs2p[g] for g in crossing_outcome_genotype])
        u, ind, c = np.unique(crossing_outcome_color, return_counts=True, return_inverse=True)
        color_count = c[ind]
        old_geno = np.isin(crossing_outcome_genotype, had)
        output_order = np.lexsort((color_count, old_geno))

        crossing_outcome_genotype = crossing_outcome_genotype[output_order]
        crossing_outcome_color = crossing_outcome_color[output_order]
        old_geno = old_geno[output_order]
        color_count = color_count[output_order]

        comb_result.append("""            <tr>
                <td style="background-color: {p1color}">{p1gene}</td>
                <td>&#215</td>
                <td style="background-color: {p2color}">{p2gene}</td>
                <td>=</td>""".format(p1gene=p1gene, p2gene=p2gene, p1color=color_dict[fl.gs2p[p1gene]], p2color=color_dict[fl.gs2p[p1gene]]))

        for ii in list(range(len(crossing_outcome_genotype))):
            if not old_geno[ii] and color_count[ii] == 1:
                comb_result.append("""                <td style="background-color: {f1color}; border: 1px solid black">{f1gene}</td>""".format(f1gene=crossing_outcome_genotype[ii], f1color=color_dict[crossing_outcome_color[ii]]))
            else:
                comb_result.append("""                <td style="background-color: {f1color};">{f1gene}</td>""".format(f1gene=crossing_outcome_genotype[ii], f1color=color_dict[crossing_outcome_color[ii]]))
        comb_result.append("            </tr>")

        if min(color_count) == 1 and min(old_geno.astype(int)) == 0:
            str1.append("\n".join(comb_result))
        else:
            str2.append("\n".join(comb_result))

    htmlf.write("\n".join(str1))
    htmlf.write("\n".join(str2))
            
    htmlf.write("""
        </table>
    </div>
</body>
</html>""")
