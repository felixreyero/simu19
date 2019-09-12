def gcl(x_n):
   m = 7             # modulus
   a = 3              # multiplier
   c = 0              # increment Podría ser c=7, pero c debe ser menor a m. 

   x = ((a * x_n) + c) % m

   return x

x_1 = 6

for _ in range(50):
   x_1 = gcl(x_1)
   print(x_1)
#En el parcial piden saber cuántas veces entra la secuencia en 51:
#La primer secuencia es 6 4 5 1 3 2 6 4.
#Multiplicado por 8 veces, entra entera la secuencia. Siendo el X49=6, X50=4 y X51=5
