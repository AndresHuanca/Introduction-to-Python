myVariable = "Hello mister Andres"

print(myVariable)
print(myVariable)

myVariable = 10
print(myVariable)

myVariable = True
print(myVariable)

myVariable = False
print(myVariable)

x = 10
y = 20
z= x+y
print(x)
print(y)
print(z)

#Data Types
#referencia Ram
a = "Andres"
print(id(a))
print(type(a))
b: str = "Hola"
print(b)

#Concatenacion
group = "Juanes "
myName = "Andres"
other = "Hola "+ "Mundo"
print("Mi grupo favorito es : " + group + other)

#numbers sum concanted
number01 = "10"
number02 = "50"
print("Concated : " + number01 + number02)
print("Suma : ", int(number01) + int(number02) )

#Boolean
date01 = True
#Hace la pregunta y se asigna nuevo valor
date01 = 1 < 0
print(date01)

#if
if date01:
    print("date01 is True")
else:
    print("date01 is False")

#Input

#result = input("Enter data : ")
#print("Entered value ", result)
#print("finish input")

#concated
#nu01 = input("ingresar numero : ")
#nu02 = input("ingresar numero : ")

#result = nu01 + nu02
#print("the result is : ", result)

#sum
#nu01 = int(input("ingresar numero : "))
#nu02 = int(input("ingresar numero : "))

#result = nu01 + nu02
#print("the result is : ", result)

#Exercise

nu01 = input("Como estuvo tu dia (1-10) : ")
print("Result : ", nu01)