#!/usr/bin/env python3

"""
Usage: ./week1dnds.py <dna blast> <aa maffta align>
"""
#Plot synon and nonsynon muts; comp nts at positions in other sequences.


import fasta
import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests


prot = open(sys.argv[1])
dna = open(sys.argv[2])

dna_reader = fasta.FASTAReader(dna)
prot_reader = fasta.FASTAReader(prot)

 
n_seq = []
main_aaseq =[]


for (dna_id, dna), (aa_id, aa) in zip(dna_reader, prot_reader):
	dna_mod = []
	aa_mod = []
	j = 0
	for i in range(len(aa)):
		a = aa[i]
		n = dna[j: j + 3]
		
		if a == '-':
			n = "---"
			dna_mod.append(n)
			aa_mod.append(a)
		else:
			j+=3
			dna_mod.append(n)
			aa_mod.append(a)
	
	n_seq.append(dna_mod)
	main_aaseq.append(aa_mod)


qaa_list = main_aaseq[0]
qdna_list = n_seq[0]


dN = [0] * len(qaa_list)
dS = [0] * len(qdna_list)




for i in range(1, len(main_aaseq[1:])):
	list_align = main_aaseq[i]
	
	for j in range(len(list_align)):
		if list_align[j] != qaa_list[j]:
			dN[j] += 1
		else:
			dS[j] += 1
		
ratio_list = []
for i in range(len(dS)):
	dSN = dN[i] / (dS[i] + 1)
	ratio_list.append(dSN)


ztest = stests.ztest(dN, dS)
print(ztest)


fig, ax = plt.subplots()
plt.scatter(range(0, len(ratio_list)), ratio_list, alpha = 0.5, s = 3, color ='blue')
ax.set_ylabel("ratio dN/dS")
ax.set_xlabel("amino acid position")
ax.set_title("Ratio of synonymous nonsynonymous nt changes based on amino acid position")

plt.tight_layout()
fig.savefig("wk1dS_dN.png")
plt.close(fig)

