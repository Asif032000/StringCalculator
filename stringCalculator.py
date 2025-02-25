import re

def add(numsString):
    match = re.match('^//.*\s', numsString)
    
    if match:
        # all delimiters string
        delimitersString = numsString[match.start()+2 :match.end()-1 ] #parse dynamic delimiter
        allMatches = re.findall(r'\[(.*?)\]', delimitersString)
        numsString = numsString[match.end():]       # numbers string to work upon
        for delimiter in allMatches:
            numsString = numsString.replace(delimiter, ",")     # replace all delimiters with ","
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