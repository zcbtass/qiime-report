#!/bin/bash --login
#PBS -l walltime=02:00:00
#PBS -l select=1:ncpus=36
#PBS -N OTU_Network_closed_no_colour
#PBS -A d411-training
cd $PBS_O_WORKDIR
module load miniconda/python2
export TMPDIR=~/qiime_tmp
echo "loading virtualenv"
source activate qiime1

time make_otu_network.py \
-i ~/2018_02_smb/closed/otu_table.biom \
-m ~/2018_02_smb/map.tsv \
-o ~/OTU_network

source deactivate
