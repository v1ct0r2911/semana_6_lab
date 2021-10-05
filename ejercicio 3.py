a= int(input("escriba el costo total de la compra: "))
if a>1000:
    descuento=a*0.20
    compra_total= a-descuento
    print("total a pagar es: ", compra_total)
else:
    print("no hay descuento ",a)