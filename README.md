# Find new sequencing technologies in the scRNAseq database

This repository contains one method to find all sequencing technologies in scRNAseq database. scRNASeqDB is developed and curated by UT Health to facilitate the understanding of transcriptome in a single cell. It contains 36 single cell gene expression datasets from GEO involving 8910 cells from 174 cell groups. It features heatmap, boxplot of gene expression, gene correlation matrix, GO and pathway annotation. 

I wonder if there's some new sequencing technologies emerging in this field, to this end this is what the repository can do.

Make a new directory and enter.
`mkdir ./scrnaseqdb_browse_page`

First `curl` the 'browse' section of the webpage.

```
curl https://bioinfo.uth.edu/scrnaseqdb/index.php\?r\=gseTable/browse\&csrt\=4013180899601809099 -o page1.html
curl https://bioinfo.uth.edu/scrnaseqdb/index.php\?r\=gseTable/browse\&csrt\=4013180899601809099 -o page2.html
curl https://bioinfo.uth.edu/scrnaseqdb/index.php\?r\=gseTable/browse\&csrt\=4013180899601809099 -o page3.html
curl https://bioinfo.uth.edu/scrnaseqdb/index.php\?r\=gseTable/browse\&csrt\=4013180899601809099 -o page4.html
```

Then we have four html files. Then use `get_GEO_from_scrnaseqdb.py` to get GEO page from the 4 html files and create a text file storing the result.
`python3 get_GEO_from_scrnaseqdb.py > GEO_in_db.txt`

Use `wget` to recursively download the html page from the text file and store them in the `geo_dir` directory. You may need to create the `geo_dir` directory first.
`wget --directory-prefix geo_dir --input-file GEO_in_db.txt`

Finally use `find_design.py` to parse the html files to get the word ending with "-seq".
`python3 find_design.py | grep -o '\b[-[:alnum:]]*seq\b'`

The output result is:
```
SUPeR-seq
RNA-seq
SUPeR-seq
RNA-seq
SMART-seq
RNA-seq
RNA-seq
RNA-seq
SMART-seq
RNA-seq
SMART-seq
RNA-seq
RNA-seq
SMART-seq
RNA-seq
RNA-seq
RNA-seq
RNA-seq
SUPeR-seq
RNA-seq
SUPeR-seq
SMART-seq
RNA-seq
RNA-seq
RNA-seq
SMART-seq
RNA-seq
RNA-seq
SMART-seq
RNA-seq
RNA-seq
SMART-seq
RNA-seq
RNA-seq
RNA-seq
RNA-seq
```
in other words we only have RNA-seq, SMART-seq and SUPeR-seq keywords available in the scRNAseq database.
