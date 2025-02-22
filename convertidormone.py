# Moneda

co = int(input("Digita cuanto tienes en pesos colombiano: "))
tco = co*0.00025
print(f"esto tienes USD: {tco}")

pe = float(input("digista cuanto tienes en soles perunao: "))
tpe = pe*0.27
print (f"Esto tienes USD: {tpe}")

br = float(input("Digita cuanto tienes en reales brasileño: "))
tbr = br*0.175
print (f"Esto tienes USD: {tbr}")

#total = co*0.00025 + pe*0.27 + br*0.17550
total = tco + tpe + tbr

print(f"en dinero colombia tienes ${tco}, en dinero peruano tienes ${tpe} y en dinero brasileño tienes ${tbr} ")
print(f"tienes un total en USD $ {total}")
