""" steps for week3 assignment in shell"""

# install programs required
# command: install freebayes bwa vcflib vcftools snpeff

# download files from links and move to week3 directory
# tar -xf <tar.xv> file

# bwa index <fna file>

# mapping against sacCer3 genome build (iterate through 10 files)
# bwa mem -t 8 -o A01_09.sam -R "RG\tID:A01_09\tSM:A01_09" GCF_000146045.2_R64_genomic.fna A01_09.fastq

# sort and convert sam to bam files (iterate through all ten files)
# samtools sort -O BAM -o A01_09.bam A01_09.sam

# call variants and create VCF with freebayes
# freebayes -f GCF_000146045.2_R64_genomic.fna A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam > freebayes_out.vcf

# filter based on genotype quality and decompose complex haplotypes
# vcffilter -f "QUAL > 20" freebayes_out.vcf | vcfallelicprimitives > results.vcf

# load database for R64-1-1
# snpEff download R64-1-1.86

# annotate vcf file
# snpEff R64-1-1.86 results.vcf > results.ann.vcf

