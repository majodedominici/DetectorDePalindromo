## La consigna del trabajo es realizar un detector de palíndromos, es decir, que la palabra se lea tanto de izquierda a
# derecha y de, derecha a izquierda por igual

igual, aux = 0, 0
texto=input("Ingrese la palabra que desea evaluar: ")

for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1