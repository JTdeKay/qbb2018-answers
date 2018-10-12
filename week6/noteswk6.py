"""Set up for plotting"""

# downloading files
# mm10 chr19 from web <chr19.fa>
# CTCF and ER4/GE1 files from bxlab
# tar -xvf g1e.tar.xz
# download Mus_musculus.GRCm38.94_features.bed 

# conda macs environment creation and use:
# conda create -n macs2 macs2
# source activate macs2
# source deactivate

# bowtie2-build chr19.fa chr19_index
# bowtie2 -p 8 -x chr19_index -q CTCF_ER4.fastq -S CTCF_ER4.sam
# bowtie2 -p 8 -x chr19_index -q CTCF_G1E.fastq -S CTCF_G1E.sam

# macs2 callpeak -t CTCF_ER4.sam -c input_ER4.sam -f SAM --name ER4
# macs2 callpeak -t CTCF_G1E.sam -c input_G1E.sam -f SAM --name G1E
# bedtools intersect -a ER4_peaks.narrowPeak -b G1E_peaks.narrowPeak -v > peaksgained
