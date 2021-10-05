operador= input("ingrese la operacion: ")
a = int(input("ingrese el valor de la a: "))
b = int(input("ingrese el valor de la b: "))
if operador == "S":
    print("la suma es: ",a+b)
elif operador == "R":
    print("la resta es; ", a-b)
elif operador == "M":
    print("la multiplicacion es: ",a*b)
elif b !=0 and operador == "D":
    print("la multiplicacion es: ",a/b)
elif b==0:
    print("error") 