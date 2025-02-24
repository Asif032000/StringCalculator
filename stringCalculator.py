def add(numsString):
    if numsString == "":
        return 0
    nums = numsString.split(",")
    return sum(map(int, nums))