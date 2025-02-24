import re

def add(numsString):
    match = re.match('^//.*', numsString)
    if match:
        delimiter = numsString[2]
        numsString = numsString[4:]
        numsString = numsString.replace(delimiter, ",")
    nums = numsString.replace(",", " ").replace("\n", " ").split()      #replace "," and "\n" with " " and then split
    numsInt = list(map(int, nums))
    negativeNumbers = []
    for num in numsInt:
        if num < 0:
            negativeNumbers.append(str(num))
    if len(negativeNumbers) > 0:
        errorMessage = 'negative numbers not allowed ' + (",").join(negativeNumbers)
        raise ValueError(errorMessage)
    return sum(numsInt)