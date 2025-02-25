import re

def add(numsString):
    match = re.match('^//.*\s', numsString)
    
    if match:
        delimiter = numsString[match.start()+2 :match.end()-1 ] #parse dynamic delimiter
        numsString = numsString[match.end():]
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
    #ignore numbers greater than 1000
    numsInt = filter(lambda x:x<1001, numsInt)
    return sum(numsInt)