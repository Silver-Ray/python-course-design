counter = 1
i = 1
for counter in range(1,10,1):
    for i in range(1,counter+1, 1):
        z = counter * i
        print("%d*%d =%d"%(counter,i,z),end = "\t")
    print("\n")