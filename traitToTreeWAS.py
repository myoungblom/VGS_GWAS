#!/usr/bin/env python

import sys
from Bio import Phylo

#####
# This script takes in a traits file, a trait of interest (header in traits file)
# and a newick tree (to be used with TreeWAS) and outputs a phenotype file
# to be used with TreeWAS.
#####

# check for correct arguments
if len(sys.argv) != 4:
    print("Usage: scoaryToTreeWAS.py <traits.csv> <trait> <tree.newick>")
    sys.exit(0)

traitFile = sys.argv[1]
trait = sys.argv[2]
treefile = sys.argv[3]

# parse scoary traits file for given trait into dictionary
traitDict = {}
with open(traitFile, "r") as f:
    for line in f:
        info = line.strip().split(",")
        if line.startswith(","):
            headindex = info.index(trait)
        elif not line.startswith(","):
            pheno = info[headindex]
            isolate = info[0]
            traitDict[isolate] = pheno

# read tree file using Bio.Phylo
tree = Phylo.read(treefile, "newick")
terminals = tree.get_terminals()

output = open(header+"_treewasPheno.txt", "w")
output.write("ID\t"+header+"\n")

# write phenotype from scoary traits in order of tips in tree
for i in terminals: 
    term = i.name
    output.write(term+"\t"+traitDict[term]+"\n")

output.close()
