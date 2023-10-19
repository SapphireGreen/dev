"""
def search_str(file_path, word):
    with open(file_path, 'r', encoding="utf8") as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print('string exist in a file')
        else:
            print('string does not exist in a file')

search_str(r'kazam-qrh55z.txt', 'qrh55z')

"""
import os

word = 'qrh55z'
with open(r'kazam-qrh55z.txt', 'r', encoding="utf8") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            output_filename = os.path.normpath("output.log")
            # Overwrites the file, ensure we're starting out with a blank file
            with open(output_filename, "w", encoding="utf8") as out_file:
                out_file.write("")

            # Open output file in 'append' mode
            with open(output_filename, "a", encoding="utf8") as out_file:
                out_file.write(line)
            
            