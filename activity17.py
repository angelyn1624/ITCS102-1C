for x in range(1,16,1):
    for y in range(16,x,-1):
        print("@",end="")
    for u in range(1,x,1):
        print("#",end="")
    print()
