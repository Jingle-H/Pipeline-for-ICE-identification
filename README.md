# ICE Identification Pipeline

This repository contains a pipeline for identifying Integrative Conjugative Elements (ICEs) in Metagenome-Assembled Genomes (MAGs). The workflow integrates multiple bioinformatics tools to detect conjugation systems, gene islands, and associated mobile genetic elements.

## Dependencies
- [Mauve](http://darlinglab.org/mauve/mauve.html) (v2015.02.13+)
- [Prokka](https://github.com/tseemann/prokka) (v1.14+)
- [Prodigal](https://github.com/hyattpd/Prodigal) (v2.6+)
- [MacSyFinder](https://github.com/gem-pasteur/macsyfinder) (v2.0+)
- [Islandviewer](https://www.pathogenomics.sfu.ca/islandviewer/) (v4.0+)
- Python (v3.7+)

## Workflow Overview

### Step 1: Prepare query_list.txt file
### Step 2: MAG Reordering using Mauve
### Step 3: Contig Stitching
### Step 4: Conjugation System Detection using MacSyFinder
### Step 5: Gene Island Prediction using Islandviewer
### Step 6: ICE Component Verification
### Step 7: ICEberg Comparison

## Acknowledgments
We sincerely thank Professor [Nolan Woods](https://www.sfu.ca/computing/people/faculty/nolanwoods.html) from Simon Fraser University for providing the `stitch.py` script. Professor Woods is a key developer of the [IslandViewer](https://www.pathogenomics.sfu.ca/islandviewer/) software, and his expertise in genomic island analysis was invaluable to this project.

Special thanks for his guidance on:
- Contig stitching methodology
- Handling fragmented assemblies
- Integration of genomic island prediction techniques
