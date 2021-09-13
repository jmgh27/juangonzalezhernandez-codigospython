print("Evaliacion credicticia, registre los datos que se le solicitan por favor")
nom= input("Nombre: ")
eda= input("Edad: ")
ing= input("Ingreso mensual: ")
egr= input("Egreso mensual: ")
pre= input("Cantidad del prestamo a solicitar: ")
pag= input("Meses a pagar: ")


eda= int(eda)
ing= int(ing)
egr= int(egr)
pre= int(pre)
pag= int(pag)


tot=ing-egr
cuo=pre/pag

if eda<18 or ing < egr or tot < cuo:
    print("No cumple con los requisitos para obtener el credito")

else :
    print("Cumple con los requisitos para obtener el credito")
