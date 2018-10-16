jindagi='y'
while jindagi=='y':
    from module1 import stock
    def call():
        from module3 import update
        return update()
    print("Products"+"\t\t"+"Price"+"\t\t"+"Quantity"+"\t"+"Product No")
    f=0
    g=0
    for i in stock():
        print(str(i[f])+"\t\t\t"+str(i[f+1])+"\t\t"+str(i[f+2])+"\t\t"+str(g))
        g=g+1
    print(call())
    jindagi=input("Create a new invoice?(y/n)")
