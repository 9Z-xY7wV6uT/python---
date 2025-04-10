i,k,a,b = 0,0,"",""

#real code#
for i in range(2,10,1) :
    a = a + ("#    %d단   #"%(i))
print(a)
for i in range(1,10,1) :
    b = ""
    for k in range(2,10,1) :
       b = b + ("%2d x %2d = %2d"%(k,i,i*k))
    print(b)     

    