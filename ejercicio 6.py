monto =int(input("ingrese monto:"))
if monto<100:
    print("no hay comicion: ")
else:
    if monto<300:
        print("la comicion es: ", monto*0.10)
    else:
        print("la comicion es: ",monto*0.20)    
