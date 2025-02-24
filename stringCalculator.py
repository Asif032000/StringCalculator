def add(numsString):
    nums = numsString.replace(",", " ").replace("\n", " ").split()      #replace "," and "\n" with " " and then split
    return sum(map(int, nums))