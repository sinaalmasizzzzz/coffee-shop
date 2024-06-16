import Function
a=list()
while True:
    print(Function.List())
    code=input("Submit the product code you want: ")
    x=Function.read("Code","Number",code)
    x1=str(x+1)
    Function.edith(x1,code)
    z=input("How much do you want from that product: ")
    for i in range(int(z)):
        a.append(Function.read("Code","Price",code))
    
    x=input("Do you still want to?\n1=Yes\n2=No")

    if x=="1":
        ...
    elif x=="2":
        break
z=0
for i in a:
    z=z+i
print(z)