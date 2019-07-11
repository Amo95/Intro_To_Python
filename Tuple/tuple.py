def partition():
    ran = range(1,10)
    tup1 = ()
    tup2 = ()
    for a in ran:       
        if a % 2 != 0:
            tup2 = a
            print("\t",tup2)
        
    for r in ran:
        if r % 2 == 0:
            tup1 = r
            print(tup1)
    
partition()

