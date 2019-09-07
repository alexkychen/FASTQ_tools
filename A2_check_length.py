#A2_check_length.py: check sequence length of multiple FASTQ files in a directory
import gzip
import glob

file_ls=glob.glob('*.fastq.gz') #identify all fastq.gz files and make them a list
number_of_file=len(file_ls) #count number of files

if number_of_file == 0:
    print("No FASTQ files were found.")
else:
    for files in file_ls:
        with gzip.open(files,'rb') as f:
            count=0
            for line in f:
                count=count+1
                if count==1: continue
                if count==2:
                    line=line.rstrip()
                    seq_length=len(line)
                    print(files,line,seq_length)
                else: break
