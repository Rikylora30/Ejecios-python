# -- coding: utf-8 --

n1 = int(input("\nIngrese un Numero: "))
n2 = int(input("\nIngrese otro Numero menor al anterior: "))

while n1 < n2:
	n2 = int(input("\nIngrese otro Numero menor al anterior: "))
	
	
if n1 > n2 or n1 == n2:

	while n1 != n2:
		p = n1 - n2
		n1 -= 1
		print "\nFaltan:%d numeros" % p
	print "\nEl programa Termino"   

	