def hanoi(n,src,dest,temp):
    if n>=1:
        hanoi(n-1,src,temp,dest)
        print("move %d-->%d"%(src,dest))
        hanoi(n-1,temp,dest,src)
hanoi(3,1,3,2)
