N=list(input("Enter a binary number :"))
x =0
for i in range (len(N)) :
    number =N.pop()
    if number =='1' :
        x= x + pow(2,i)
print("The decimal result of number is " , x)
