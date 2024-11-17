def binarysearch(alist,item):
    first=0
    last=len(alist)-1
    found=False
    while first<=last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True
        else:
            if item<alist[midpoint]:
                 last=midpoint-1
            else:
                first=midpoint+1
    return found
testlist=[0,1,2,8,13,17,19,32,42]
item=int(input('Enter the number you want to search:'))
isitfound=binarysearch(testlist,item)
if isitfound:
    print('Your number is in the list')
else:
    print('You number is not in the list')
                
