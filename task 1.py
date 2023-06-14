def prefixsum(thelist,x2,x1):
    mylist = [0]*len(thelist)
    mylist[0] = thelist[0]
    for i in range(1, len(thelist)):
        mylist[i] = mylist[i-1] + thelist[i]
    
    return mylist[x2] - mylist[x1]