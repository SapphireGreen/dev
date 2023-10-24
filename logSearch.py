#import resource
import os
import re

file_name = "kazam-qrh55z.txt"

"""
path = rf"C:\Users\HP\Documents\dev\Logs\{device_id}"
>>> path
'C:\\Users\\HP\\Documents\\dev\\Logs\\xyz'
"""
output_filename = os.path.normpath("output1.log")
regex = r"{\s*device_id:\s*'do0142'[\s\S]*?}(?=\n\n|$)"


with open("kazam-qrh55z.txt", 'r', encoding="utf8") as input:
    line = input.read()

with open("output1.log", 'w', encoding="utf8") as output:

    matches = re.finditer(regex, line, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):

        #print ("{match}".format(match = match.group()))
        output.write("{match}".format(match = match.group())+'\n')

print("file created successfully")

