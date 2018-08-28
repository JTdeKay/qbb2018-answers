#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTE=../genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
    echo "running $SAMPLE"
    mkdir $SAMPLE
    echo "running hisat2 $SAMPLE"
    hisat2 -x ~/qbb2018-answers/genomes/BDGP6 -U ~/qbb2018-answers/rawdata/${SAMPLE}.fastq -S ${SAMPLE}/alignment.sam
    echo "running samtools view $SAMPLE"
    samtools view -b ${SAMPLE}/alignment.sam -o ${SAMPLE}/alignment.bam
    echo "running samtools sort $SAMPLE"
    samtools sort ${SAMPLE}/alignment.bam -o ${SAMPLE}/alsorted.bam
    echo "running samtools index $SAMPLE"
    samtools index ${SAMPLE}/alsorted.bam
    echo "running stringtie $SAMPLE"
    stringtie ${SAMPLE}/alsorted.bam -G $ANNOTE -o ${SAMPLE}/output.gtf -e -p 8 -B


done
