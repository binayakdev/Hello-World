def update():
    from module1 import stock
    from module2 import invoice
    z=invoice()
    x=stock()
    for i in range(len(x)):
        for j in range(len(z)):
            if x[i][0].upper()==z[j][0].upper():
                x[i][2]=int(x[i][2])-int(z[j][1])
    file=open("Stock.txt","w")
    i=0
    b=x
    a=[]
    for i in range(len(b)):
        a.append([b[i][0],b[i][1],b[i][2]])
    print(a)
    for m in a:
        y=0
        for n in a:
            file.write(str(n[y]))
            file.write(str(','))
            file.write(str(n[y+1]))
            file.write(str(','))
            file.write(str(n[y+2]))
            file.write('\n')
        break
    file.close()
    return("Updating......")


