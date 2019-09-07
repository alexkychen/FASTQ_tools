#B2_trim.py: Trim sequence length of multiple FASTQ files in a folder
import gzip
import glob

#Enter new sequence length
try:
    trim=raw_input('New sequence length: ')
except:
    trim=input('New sequence length: ')

file_ls=glob.glob('*.fastq.gz') #identify all fastq.gz files and list it
number_of_file=len(file_ls) #count number of files

if number_of_file == 0:
    print("No FASTQ files were found.")
else:
    print(number_of_file,'files are found.')
    for files in file_ls:
        outfile_name=files.rstrip('.fastq.gz')+'_'+trim+'.fastq.gz'
        with gzip.open(files,'rb') as f,gzip.open(outfile_name,'wb') as f_out:
            for line in f:
                line=line.rstrip()
                line_x=line[0:int(trim)]
                f_out.write(line_x+'\n')
