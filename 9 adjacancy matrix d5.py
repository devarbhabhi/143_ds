print("Enter dwtails of grtaph")
x=int(input("Enter no of nodes"))
a=[[0 for i in range(6)] for j in range(6)]
print("insert node vise edages")
for i in range(0,x):
    print("enter no of eage coming out from node",i)
    y=int(input("no of egdes"))
    for j in range(0,y):
        ed=int(input("end node"))
        a[i][ed]=1
    print("\n")
print("abjacancy matrix")
for i in range(0,x):
    for j in range(0,x):
        print(a[i][j],end="")
    print(end="\n")
