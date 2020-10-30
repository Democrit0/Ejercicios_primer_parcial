def suma(a,b):
  resultado = a + b
  return resultado
def resta(a,b):
  resultado = a - b
  return resultado
def producto(a,b):
  resultado = a*b
  return resultado
def division(a,b):
  b_ = b
  while b_==0:
    print("Valor incorrecto")
    b_=float(input("numero distinto de cero: "))
  return a/b_  
  