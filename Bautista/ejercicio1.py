def gcl(x_n):
   m = 10             # modulus
   a = 1              # multiplier
   c = 7              # increment

   x = ((a * x_n) + c) % m

   return x

x_7 = 7
x_1 = 1

print("Con semilla 7")
for _ in range(11):
   x_7 = gcl(x_7)
   print(x_7)

print("Con semilla 1")
for _ in range(11):
   x_1 = gcl(x_1)
   print(x_1)
