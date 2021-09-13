re1 = float(input("Valor de la primer resistencia: "))
re2 = float(input("Valor de la segunda resistencia: "))
ret=(re1*re2)/(re1+re2)
print("Valor de la resistencia total en paralelo "+ str(ret)+ " ohms")
