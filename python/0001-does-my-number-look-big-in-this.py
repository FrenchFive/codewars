num = 153

def narcissistic( value ):
    strnum = str(value)
    length = len(strnum)

    total = 0
    for i in range(length):
        total +=  pow( int(strnum[i]) , length)

    if total == value:
        return(True)
    else:
        return(False)

print(narcissistic(num))