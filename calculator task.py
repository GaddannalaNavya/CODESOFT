num1=float(input("enter the 1 number: "))
num2=float(input("enter the 2 number: "))
operator=input("enter the operator(+ - * /  %):")
if operator=="+":
    print("result=",num1+num2)
elif operator=="-":
    print("result=",num1-num2)
elif operator=="*":
    print("result=",num1*num2) 
elif operator=="/":
    print("result=",num1/num2)       
elif operator=="%":
    print("result=",num1%num2)
else:
    print("operator is not valid")