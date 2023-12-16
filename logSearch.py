#import resource
import os
import re

file_name = "kazam-ww-su-log-04-0-01-24-11-2023.txt"

device_id = "u9oi9b"
log_date = "_23-11-2023"

path = rf"C:\Users\HP\Documents\dev\Logs\{device_id + log_date}"

output_filename = os.path.normpath(path)
regex = r"{\s*device_id:\s*'u9oi9b'[\s\S]*?}(?=\n\n|$)"


with open(file_name, 'r', encoding="utf8") as input:
    line = input.read()

with open(output_filename+".txt", 'w', encoding="utf8") as output:

    matches = re.finditer(regex, line, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):

        #print ("{match}".format(match = match.group()))
        output.write("{match}".format(match = match.group())+'\n')

print("file created successfully")

