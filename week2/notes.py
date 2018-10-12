"""Week 2 assignment notes"""

# import tools
# conda install velvet spades lastz

# download data files < reads_low_1.fastq and reads_low_2.fastq

# assemble reads as contigs using velvet
# velveth Assem 31 -shortpaired -separate -fastq
# velvetg
# dir Assem: contigs.fa, stats.txt, etc.

# assemble reads with SPAdes
# spades.py -1 t -2 --o ./spades_low --only-assembler -k 31 -o SPAdes_output

# download reference genome <reference.fasta>
