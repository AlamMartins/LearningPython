print("Hello, World!")

print("---------------------------------------")
                #String Variables

age = 18      # age is of type int
name = "John" # name is now of type str
print(name)

print("---------------------------------------")
                #String Slicing

msg = "Hello, World!"
print(msg[2:5])

print("---------------------------------------")
                    #Array

mylist = []
mylist.append(1) #Adicionando valores no array
mylist.append(2)

for item in mylist:
    print(item) # prints out 1,2

    
print("---------------------------------------")
            #If Statements

#Validando apenas uma condição
num = 200
if num > 0:
    print("Valor da variavel e maior que 0")
else:
    print("Valor da variavel e menor que 0")


        #Aplicando mais de uma condição
num = 3
if num > 0:
    print("Valor da variavel e maior que 0")
elif num == 0:
    print("Valor da variavel e igual a 0")
else:
    print("Valor da variavel e menor que 0")

    
print("---------------------------------------")
                #Looping

for item in range(30): #Parâmetro que indica o número de repetições
    if item == 3: break #Validação que interrompe o looping
    print(item)    #Imprime os valores 0,1,2 do resulado
else:
    print("Finally finished!") #Imprime quando o looping termina caso não atenda a condição de parada


print("---------------------------------------")
                #Functions 1

#Criando um contador
def my_function():
    counter = 0
    while counter < 5:
        print("Hello from a function: ",counter)
        counter += 1
    print("Hello from a function: ",counter) 

def main():
    my_function()
  


main()
     
print("---------------------------------------")

                #Functions 2
numero = 50
def check_number(numero):
    if numero > 0:
        print("Positive number")
    elif numero == 0:
        print("Zero")
    else:
        print("Negative number")

check_number(numero)

print("---------------------------------------")

                #Functions 3

class Carteira:
    def __init__(self, saldo):
        self.saldo = saldo

    def soma(self, valor):
        self.saldo += valor

    def subtrai(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def retira(self, valor):
        self.subtrai(valor)
        self.saldo -= 0.5
 