print("      ****************")
print("      ****Tabuada!****")
print("      ****************\n")

numero = int(input("Infome, qual tabuada você quer?\n"))
resultado = 0
sair = 1
print("0 - Sair")
while sair:
   for tab in range(11):
      resultado = numero * tab
      print(numero, "X", tab, "=", resultado)
   sair = int(input("Digite 1 para coninuar e 0 para sair\n"))
   if sair == 0:
       break;
   while sair != 0 and sair!= 1:
       print("Número digitado está INCORRETO!!!\n")
       sair = int(input("DIGITE 1 PARA CONTINUAR E 0 PARA SAIR\n"))
   if sair == 0:
       break;
   numero = int(input("Infome, qual tabuada você quer?\n"))