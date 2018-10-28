""" Notes for week8 QBB motif homework"""

# Generated peak calls file downloaded < ER4_peaks.narrowPeak >
# wget "https://raw.githubusercontent.com/bxlab/qbb2018/master/data/ER4_peaks.narrowPeak"

# sort peak file
# sort -nk 8 ER4_peaks.narrowPeak | tail -100 > peaks100.out

# Mm chr19 to working directory
# cp from week6 to week8 directory

# MEME 
# conda install meme
# MEME motif databases downloaded 
# JASPAR_CORE_2016.meme copied to working directory

# convert peak file to fasta for passing to MEME
# bedtools getfasta -fi chr19.fa -bed peaks100.out -fo soi.out

# motif finding in top 100 peaks of ER4 state
# meme-chip soi.out
# visualize motif at meme-chip.html

# tomtom 