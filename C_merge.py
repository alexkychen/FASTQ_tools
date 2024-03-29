#C_merge.py: Merge R1 and R2 reads of paired-end sequence data

import sys
import gzip
from itertools import izip #see ref. link:http://stackoverflow.com/questions/27997400/how-to-join-two-text-files-with-python

#Enter file
try:
    R1=raw_input('Enter R1 file including .fastq.gz: ')
except:
    R1=input('Enter R1 file including .fastq.gz: ')
try:
    f1=gzip.open(R1,'rb')
except:
    print('File cannot be found '+R1)
    sys.exit()
try:
    R2=raw_input('Enter R2 file including .fastq.gz: ')
except:
    R2=input('Enter R2 file including .fastq.gz: ')
try:
    f2=gzip.open(R2,'rb')
except:
    print('File cannot be found '+R2)
    sys.exit()

#Check length of R1 and R2 files
try:
    ans=raw_input('Do you want to check lines in R1/R2 files? (Y or N): ')
except:
    ans=input('Do you want to check lines in R1/R2 files? (Y or N): ')

if ans.upper()=='Y':
    count1=0
    for line in f1:
        count1=count1+1
        if (count1 % 1000)==0:
            sys.stdout.write('\rCounting R1 '+str(count1)+' lines.')
            sys.stdout.flush()
    print('\rR1 has total '+str(count1)+' lines.')
    count2=0
    for line in f2:
        count2=count2+1
        if (count2 % 1000)==0:
            sys.stdout.write('\rCounting R2 '+str(count2)+' lines.')
            sys.stdout.flush()
    print('\rR2 has total '+str(count2)+' lines.')

    if count1==count2:
        print('R1 and R2 are looking good.')
    if count1!=count2:
        print('R1 and R2 have different number of lines. Please double check.')
        sys.exit()
else:
    print('continue...')

#Enter outfile name
try:
    outfile=raw_input('Next, enter outfile name including .fastq.gz: ')
except:
    outfile=input('Next, enter outfile name including .fastq.gz: ')
#Merge R1 and R2 files and write to outfile
count=0
with gzip.open(outfile,'wb') as res, gzip.open(R1,'rb') as f1, gzip.open(R2,'rb') as f2:
    for line1,line2 in izip(f1,f2):
        line2=line2.rstrip()
        line2=line2.replace('A','t').replace('T','a').replace('C','g').replace('G','c')#Make complementary seq
        line2=line2.upper()[::-1] #Make DNA seq upper case and reverse([::-1])
        res.write(line1.rstrip())
        res.write(line2.rstrip())
        res.write('\n')
        count=count+1
        if (count % 1000)==0:
            sys.stdout.write('\rMerging '+str(count)+' lines.')
            sys.stdout.flush()
    print('\nA total of '+str(count)+' lines had been merged.')
print('Done!')
