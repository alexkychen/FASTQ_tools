#A1_check_length.py: Check sequence length of a single FASTQ file.
import gzip

try:
    inputfile=raw_input('Enter file name(include .fastg.gz): ')
except:
    inputfile=input('Enter file name(include .fastg.gz): ')

try:
    with gzip.open(inputfile, 'rb') as f: #Read a single .gz file
        count = 0
        for line in f:
            count=count+1
            if count==1: #1st line is not a sequence, so continue
                continue
            if count==2: #2nd line is the sequence , so check length
                line=line.rstrip()
                seq_length=len(line)
                print(line, seq_length)
            else: # stop the program count equals to other numbers
                break
except:
    print("File not found.")
