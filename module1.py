def stock():
    file=open("Stock.txt","r")
    lines=file.readlines()
    a=[]
    for i in lines:
        s=i.replace("\n","").split(',')
        a.append(s)
        file.close()
    for x in range(len(a)):
        a[x][0]=a[x][0].upper()
        a[x][1]=int(a[x][1])
        a[x][2]=int(a[x][2])
    return a




    
    
    
    
    

