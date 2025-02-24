import re

def add(numsString):
    match = re.match('^//.*', numsString)
    if match:
        delimiter = numsString[2]
        numsString = numsString[4:]
        numsString = numsString.replace(delimiter, ",")
    nums = numsString.replace(",", " ").replace("\n", " ").split()      #replace "," and "\n" with " " and then split
    return sum(map(int, nums))