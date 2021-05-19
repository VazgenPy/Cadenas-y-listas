var=input("Escribe un texto \n")
palabras=0
if var != "":
	palabras=1
for i in range(0,len(var)):
	print(var[i], palabras)
	if var[i] == " " and var[i+1] != " " and var[i+2] != " ":
		palabras=palabras+1
if palabras >= 20:
	print("Bien")