#B1_trim.py: Trim all the sequence to desired length in FASTQ files

import gzip

#Enter a file name and new length
try:
    inputfile=raw_input('Enter file name(include .fastg.gz): ')
    trim=raw_input('New sequence length: ')
except:
    inputfile=input('Enter file name(include .fastg.gz): ')
    trim=input('New sequence length: ')

#Name output file
outfile_name=inputfile.rstrip('.fastq.gz')+'_'+trim+'.fastq.gz'

try:
    with gzip.open(inputfile,'rb') as f,gzip.open(outfile_name,'wb') as f_out:
        for line in f:
            line=line.rstrip()
            line_x=line[0:int(trim)]
            f_out.write(line_x+'\n')
except:
    print("File not found.")
