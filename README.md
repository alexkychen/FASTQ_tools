# FASTQ_tools
This repo comprises tools that help organize or preprocess FASTQ files (.fastq.gz) for downstream bioinformatic pipelines, such as AftrRAD.

After receiving FASTQ files from NGS platforms, you may want to have a quick check or preprocess the files in order to run them through downstream pipelines. Here are a few tasks that I find useful.
1. Check sequence length in FASTQ files.
2. Trim sequence reads in FASTQ files to desired lengths.
3. Merge R1 and R2 reads from paired-end sequence data.
4. Concatenate FASTQ files from the same library using bash commands (see below)

Because FASTQ files are usually large-size files (e.g., several gigabytes), it's unlikely that we can open and manipulate the files through a text editor. The best practice is to read and edit files through a program even without unzipping files. Here we provide a few Python scripts that allow you to perform the tasks on personal desktops.

# Files
1. A1_check_length.py
2. A2_check_length.py
3. B1_trim.py
4. B2_trim.py
5. C_merge.py

# How to use
First, you need to install [Python](https://www.python.org/downloads/) on your computer if you don't have one. Second, open a terminal (MacOS or Linux users) or command prompt (Windows users) and clone this repo by entering: \
`git clone https://github.com/alexkychen/FASTQ_tools.git` \
The Python files (.py) from this repo and your FASTQ files should be saved under the same directory. Next, use one of the following instructions to perform the tasks you need.

#### 1. Check sequence length of FASTQ.gz files.
Change command prompt to your working directory and enter:

`python A1_check_length.py` for a single FASTQ file, or `python A2_check_length.py` for multiple files saved under the same directory.

The A1 program will ask you to enter your FASTQ file name, and output the result.

#### 2. Trim sequence length in FASTQ.gz files.
Similarly, change command prompt to your working directory and enter:

`python B1_trim.py` for a single FASTQ file, or `python B2_trim.py` for multiple files.

The B1/B2 programs will ask you to enter a new sequence length, which must be shorter than the original length.

#### 3. Merge R1 and R2 read files for paired-end data.
Move your R1 and R2 fast.gz files and C_merge.py files under the same directory. Enter the following command in your command prompt.

`python C_merge.py`

This C_merge program will first ask you to enter R1 and R2 files to be merged, and then ask if you want to check the number of lines in the R1 and R2 files. (Number of lines/4 = Number of sequences in a file) This step is optional, but it is important to know that the number of text lines in your R1 and R2 files must be equal in order to successfully merge them. Checking number of lines in R1 and R2 may take a few seconds to minutes, depending on your data size. The script will print out the number of lines for R1 and R2 files when it finished counting, and it will also automatically detect if the number of lines in R1 and R2 is equal. If not, the program will stop and exit. The script will also ask you to enter the output file name (include .fast.gz) before starting merging the files.

#### 4. Concatenate FASTQ.gz files from the same library or samples.
In certain cases, you might have multiple sequencing runs from the same samples, it would be best to compile the data into a single file for bioinformatic pipelines. In other words, we want to concatenate two or more FASTQ files. To do so, we first need to ensure there is an empty new line at the end of your first FASTQ file such that the first line of your second FASTQ file will start at the new line when concatenating files. Here we use bash commands to complete the task.

- Step.1 Unzip FASTQ.gz files. You can simply double click the file to unzip if you’re using Mac OSX, or use [7-zip](https://www.7-zip.org/) to unzip files if using Windows.
- Step.2 Open a terminal or command prompt and change path to your working directory (use command “cd” to change path)
- Step.3 At command prompt, enter the following command.

`tail -n 4 [YourFileName].fastq`

Once you enter, you should see it outputs a few lines of text. If the new command prompt appears right after the output (not at a newline, see picture below), it means there is no newline at the end of FASTQ file. In this case, you will need to add a newline at the end of the content before concatenating two files. PS. If you have been using the programs provided here, you should not encounter such “newline” issue. \
![no new line output](/pics/nonewline.png)

If the command prompt appears at a newline in the terminal (see picture below), it means there is a newline at the end of FASTQ file and you are good to go. \
![new line output](/pics/newline.png) \

To concatenate two FASTQ files, use the following command.

`cat [FileName_A].fastq [FileName_B].fastq > [NewFileName].fastq`

Two FASTQ compressed files also can be concatenated using the following command.

`cat [FileName_A].fastq.gz [FileName_B].fastq.gz > [NewFileName].fastq.gz`

Lastly, be sure to unzip any FASTQ.gz file before running a bioinformatic pipeline if needed.

# References

1. [FASTQ format wiki](https://en.wikipedia.org/wiki/FASTQ_format)

2. Sequence example (4 lines) in FASTQ

> @SN1052:222:C5JN3ACXX:1:1101:1868:2248 1:N:0:7 \
> AGTCGATGCAGTGGTTGTTCTTGTTCTTGTCCTCATCGCTGC \
> +1 \
> CCCFFFFFHHHHHJHIJHIIJJJGIJJJJJIIJJIJJJJJJJJJJJJJGIJHJIJIJJJJ

3. [AftrRAD](https://www.ncbi.nlm.nih.gov/pubmed/25641221) bioinformatic pipeline developed by Sovic et al.
