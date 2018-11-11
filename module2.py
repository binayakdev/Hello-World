def invoice():
    list_=[]
    import datetime
    from random import randint
    from module1 import stock 
    random_num=str(randint(1111,9999))
    file=open(random_num+".txt","w")
    file.write('\t\t\t')
    file.write(str("-------------------------"))
    file.write('\n')
    file.write('\t\t\t')
    file.write(str("-------------------------"))
    file.write('\n')
    file.write('\t\t\t')
    file.write(str("    XYZ Electronics"))
    file.write('\n')
    file.write('\t\t\t')
    file.write(str("-------------------------"))
    file.write('\n')
    file.write('\t\t\t')
    file.write(str("-------------------------"))
    file.write('\n\n')
    file.write(str("Street"))
    file.write('\t\t\t\t\t\t\t')
    file.write(str("Date:"))
    file.write(str(datetime.datetime.now().day))
    file.write('/')
    file.write(str(datetime.datetime.now().month))
    file.write('/')
    file.write(str(datetime.datetime.now().year))
    file.write('\n')
    file.write(str("City, Country"))
    file.write(str('\t\t\t\t\t\t'))
    file.write(str("Invoice no:"+random_num))
    file.write('\n')
    file.write("Phone:1234567890")
    file.write('\n\n')
    file.write("*********************************************************************************")
    file.write('\n')
    file.write("*********************************************************************************")
    file.write('\n\n')
    file.write('---------------------------------------------------------------------------------')
    file.write('\n')
    file.write(str("Description"))
    file.write('\t\t\t\t')
    file.write(str("Quantity"))
    file.write('\t\t\t')
    file.write(str("Amount"))
    file.write('\n')
    file.write('---------------------------------------------------------------------------------')
    name=str(input("Enter a name: "))
    file.write('\n\n')
    file.write(str("Name: "+name))
    Amount=0
    value='y'
    while value=='y':
        product=(input("Enter a product: "))
        dev=0
        for x in range(len(stock())):
            if product.upper()!=stock()[x][0].upper():
                dev=dev+1
        if dev<len(stock()):
            file.write('\n\n')
            file.write("Product: "+product)
        else:
            print("Sorry! We do not have that product")
            product=(input("Enter product again: "))
        life=False
        while life==False:
            amount=int()
            try:
                for no in range(len(stock())):
                    no=int(input("Enter product no: "))
                    quantity=int(input("Enter number of units: "))
                    if quantity<=stock()[no][2] and quantity>0:
                        file.write('\t\t\t\t')
                        file.write(str(quantity))
                        amount=quantity*stock()[no][1]
                        file.write('\t\t\t\t')
                        file.write(str(amount))
                        life=True
                        break
                    else:
                        print("Sorry! Invalid quantity")
                        life=False
                        break
                    
            except:
                print("Invalid input")
        list_.append([product,quantity])
        Amount=Amount+amount
        value=input("Do you wish to continue?(y/n): ")
    print(Amount)
    success=False
    while success==False:
        try:
            discount=float(input("Enter discount amount: "))
            success=True
            file.write('\n\n')
            file.write(str("Discount: "+str(discount)))
        except:
            print("Invalid amount")
    total=int(Amount)-((int(discount)/100)*Amount)
    file.write('\n')
    file.write('\t\t\t\t\t\t\t\t')
    file.write("---------------")
    file.write('\n')
    file.write('\t\t\t\t\t\t\t\t\t')
    file.write(str(total))
    file.write('\n')
    file.write('\t\t\t\t\t\t\t\t')
    file.write("---------------")
    file.write('\n')
    file.write('***************************PLEASE COME AGAIN************************************')
    file.write('\n')
    file.write('--------------------------------------------------------------------------------')
    file.close()
    return list_


