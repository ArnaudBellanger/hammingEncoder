def hammingEncode(string):
    # try to imput the code in a strin 
    try:
        string = str(string)

    # if the input can't be converted in a string (the input is an object without __str__ method) return an error 
    except:
        return "Error: Input must be binary!"

    # if the execpt is not triggered we remove special character to accept different input
    string = string.replace(" ", "")
    string = string.replace("-", "")

    # return an error if there is anaything else than 0 and 1
    for c in string:
        if (c != "0") and (c != "1"):
            return "Error: Input must be binary!"
    
    if len(string)<1:
        return "Error: Input must be binary!"

    # the input is suitable to be converted using hamming encoder
    return encoding(string)

def encoding(string):
    # make a list with the postion of all the check bit
    l = len(string)
    hammingRange = [0,1]
    i = 2
    while 2**i<=(l +i):
        hammingRange.append(i)
        i+=1

    # add the check bit to the string
    for j in hammingRange:
        string = string[:2**j-1] + "X" + string[2**j-1:]

    # create a dictionary with the value of each check bit
    hammingDict = dict()
    for i in hammingRange:
        hammingDict[i]= hammingValue(i,string)

    stringList = list(string)

    for key in hammingDict:
        stringList[(2**key)-1]= hammingDict[key]

    string = ''.join(str(c) for c in stringList)
    return string


# calculate the value of each check bit
def hammingValue(i,string):
    sum = 0
    tempString =""
    # take 1 digit then skip one
    if i == 0:
        for j in range(0,len(string),2):
            tempString += string[j]
    else:
        # take 2 power i digit then skip the same amount of digit digit
        for j in range((2**i)-1,len(string),2*(2**i)):
            tempString += string[j:j+2**i]

    # avoid the first digit since it's the check bit we want to calculate
    for k in range(1,len(tempString),1):
        sum += int(tempString[k])

    return sum%2


