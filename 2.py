import os
def cls():
    os.system("cls" if os.name=="nt" else "clear")
nom = input("Dime tu nombre: ")
p = " Vazgen"
v = 100
d = 0
e = 0
z = 5
vocal = ('a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U')
nom_lower = nom[0].lower()
nom_mayus = nom[len(nom)-1].upper()
nom_medio = nom[1:-1]
while True:
	print("Hola" , nom , "tienes" , v , "puntos, que quieres hacer:")
	print("""
	1)Vol saber la  posició que està una lletra? (20 punts)
	2)Vol saber la longitut de la paraula? (20 punts)
	3)Se li pot dir quantes vegades apareix una lletra.  QUina lletra vols saber? (20 punts)
	4)Vol saber primera lletra? (20 punts)
	5)Vol saber la última lletra? (20 punts)
	6)Se li pot mostrar només les consonants de les paraules (les vocals han d'aparèixer en *). Aquesta superpista. Sol es pot demanar si ja s'ha intentat entrar alguna paraula. (40 punts). 
	7)Entrar paraula
				""")
	a = int(input("Que quieres hacer: "))
	if a == 1:
		v = v-20
		b = input("Dime la letra: ")
		print(p.find(b))
		input("Borrar")
		cls()
	elif a == 2:
		v = v-20
		print(len(p)-1)
		input("Borrar")
		cls()
	elif a == 3:
		v = v-20
		c = input("Que letra: ")
		print(p.count(c))
		input("Borrar")
		cls()
	elif a == 4:
		v = v-20
		print(p[1])
		input("Borrar")
		cls()
	elif a == 5:
		v = v-20
		print(p[len(p)-1])
		input("Borrar")
		cls()
	elif a == 6 and d >= 1:
		p = p.replace("a" , "*")
		p = p.replace("e" , "*")
		p = p.replace("i" , "*")
		p = p.replace("o" , "*")
		p = p.replace("u" , "*")
		p = p.replace("A" , "*")
		p = p.replace("E" , "*")
		p = p.replace("I" , "*")
		p = p.replace("O" , "*")
		p = p.replace("U" , "*") 
		print(p)
		v = v - 30
		input("Borrar")
		cls()
	elif a == 7:
		i = input("Pon la palabra: ")
		if " " + i == p:
			print("Felicidades" , nom_lower + nom_medio + nom_mayus , "tienes: " , v , "puntos")
			break
		elif i != p and i == p[-3:] and e == 0:
			e = e+1
			v = v+25
			z = z-1
			input("Borrar")
			cls()
		elif i != p:
			print("Mal")
			d = d+1
			v = v-15
			z = z-1
			input("Borrar")
			cls()
		if z == 0:
			break
			print("Has perdido la palabra era:" , p)