try:
    n=int(input("enter size of matrix\n"))
except:
    print("given value not valid")
try:
    a=[['z' for i in range(n)] for j in range(n)]
    print("enter matrix values")
    #for i in range(n):
     #  for j in range(n):
      #     a[i][j]=input()
    for i in range(n):
        d=input("enter values for row "+str(i)+"of length "+str(n)+"\n")
        for j in range(n):
            a[i][j]=d[j]
    print(a)
    p=input("enter START POINT\n")
    s=input("enter END POINT\n")
    for i in range(n):
       for j in range(n):
          if a[i][j]==p:
              pxcod=i
              pycod=j
          if a[i][j]==s:
              sxcod=i
              sycod=j
            
    print(str(p)+" coordinate="+str(pxcod)+","+str(pycod))
    print(str(s)+" coordinate="+str(sxcod)+","+str(sycod))

    while pxcod!=sxcod: 
       if sxcod<pxcod:
           print("move down")
           sxcod+=1
       if sxcod>pxcod:
           print("move up")
           sxcod-=1   
    while pycod!=sycod:
       if sycod<pycod:
           print("move left")
           sycod+=1
       if sycod>pycod:
           print("move right")
           sycod-=1
except:
    print("either the given values dont exist in the matix or matrix build failed")
