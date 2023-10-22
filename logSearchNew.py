# Using regular expression to find text from log heap file.

import os
import re

output_filename = os.path.normpath("outputNew.log")

device_id = "qrh55z"


p = re.compile("\{(\s|\n)(.|\n)+?\}")   # (\[.*\])
#pattern = re.compile("\[.*\]")

with open("log.txt", mode= "r", encoding="utf8") as logFile:
    log = logFile.read()
    logs = re.findall(p,log)

    print(logs)


"""
with open(output_filename, "w" ,encoding="utf8") as newOutput:
    for line in x:
        newOutput.write(str(line))
"""

print("File created for devicid id: ", device_id)