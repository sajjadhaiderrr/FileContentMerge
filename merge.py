# Glob2 to get list of files in directory
import glob2

# Output file
filename = "merged.txt"

# Get list of all text files in directory
all_text_files = glob2.glob('*.txt')

# Merge contents of all text files seperated by new line
with open(str(filename)+'.txt','w') as file_write:
    for files in all_text_files:
        filename_read = open(str(files), 'r')
        file_read = filename_read.read()
        file_write.write(file_read)
        file_write.write('\n')
