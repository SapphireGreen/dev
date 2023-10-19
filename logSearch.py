#import resource
import os

file_name = "kazam-qrh55z.txt"

print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')

txt_file = open(file_name, encoding="utf8")

count = 0
word = 'qrh55z'
output_filename = os.path("output.log")

for line in txt_file:
    # we can process file line by line here, for simplicity I am taking count of lines
    count += 1
    if line.find(word) != -1:
        # Overwrites the file, ensure we're starting out with a blank file
        with open(output_filename, "a", encoding="utf8") as out_file:
            out_file.write(line)
            

txt_file.close()

print(f'Number of Lines in the file is {count}')
