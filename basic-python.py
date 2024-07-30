#Aprendendo o básico do Python com https://cheatsheets.zip/python#python-file-handling

print("Hello, World!")

print("--------------------------------------- 1) String Variables")
    # *********** Variaveis e Strings ***********

age = 32      # Setando valor número para uma variável
name = "Alam Martins" # setando valor string para  uma variável
print(name)        # Imprime o valor da variável

print("--------------------------------------- 2) String Slicing")
    # ***********String Slicing - SUBSTRING ***********

msg = "Realizando SubString no Python!"  # Setando valor string para  uma variável
print(msg[10:20])                  #Imprimindo o valor a partir do caractere informado, é capturado do index 10 ate o 20

print("--------------------------------------- 3) Array")
   # *********** Array ***********

mylist = []      #Criando um array
mylist.append(1) #Adicionando valores no array
mylist.append(2) #Adicionando valores no array   

for item in mylist: #Looping For in 
    print(item) # prints out 1,2

    
print("--------------------------------------- 4) If Statements")
    # *********** If Statements ***********

# Validando apenas uma condição
num = 200   # Declarando uma variável com valor definido 200.
if num > 0:     # Validando se o valor da variável é maior que 0
    print("Valor da variavel e maior que 0")    # Se for maior do que 0 imprime esta mensagem
else:  # Senão
    print("Valor da variavel e menor que 0") # Imprime esta mensagem


        #Aplicando mais de uma condição
num = 3
if num > 0: # Validando se o valor da variável é maior que 0
    print("Valor da variavel e maior que 0") # Imprime esta mensagem
elif num == 0: # Validando se o valor da variável é igual a 0
    print("Valor da variavel e igual a 0") # Imprime esta mensagem
else:
    print("Valor da variavel e menor que 0") # Imprime esta mensagem

    
print("-------------------------------------- 5) Looping")
    # *********** Looping ***********

for item in range(30): #Parâmetro que indica o número de repetições
    if item == 3: break #Validação que interrompe o looping
    print(item)    #Imprime os valores 0,1,2 do resulado
else:
    print("Finally finished!") #Imprime quando o looping termina caso não atenda a condição de parada


print("--------------------------------------- 6) Função Básica com parâmetro - Função chamando outra função")
    # *********** Função Básica - Função chamando outra função ***********

#Criando um contador
def my_function(valor):
    print("Valor Recebido no parâmetro",valor)
    counter = 0 # Setando o valor 0 para o contador
    while counter < valor:      # Looping enquanto o contador for menor que 5
        print("Contador While - Counter: ",counter) # Imprime o valor do contador
        counter += 1 # Incrementando o valor do contador
    return print("Contador While Finalizado: ",counter)  # Imprime o valor do contador

def main(valor): # Função Principal
    my_function(valor)
  


main(10)
     
print("--------------------------------------- 7) Função com validação condicional")

# *********** Function with if statements ***********
numero = 50
def check_number(numero):
    if numero > 0:
        print("Positive number")
    elif numero == 0:
        print("Zero")
    else:
        print("Negative number")

check_number(numero)

print("--------------------------------------- 8) Classes e Objetos")

    # *********** Classes e Objetos ***********

class Carteira:
    saldo=0
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def retira(self, valor):
        self.subtrai(valor)
        self.saldo -= 0.5
 
 # Criando um objeto da classe Conta com um saldo inicial de 100
conta = Carteira(100)

# Depositando 50 reais na conta
conta.depositar(50)

# Sacando 20 reais da conta
conta.sacar(20)

print(conta.saldo)  # Saída: 130


print("--------------------------------------- 9) File I/O")

    # *********** Acessando Arquivos File I/O ***********

with open("c:/Users/alammartins/Desktop/py/LearningPython/bkp.txt", "r", encoding='utf8') as file: #Abrindo arquivo indicado no parâmetro
    for i, line in enumerate(file, start=1):                                                       #Looping linha por linha com o enumerate que conta as linhas  
        if '<?xml version="1.0" encoding="UTF-8"?>' in line:                                       #Validando se a palavra foi encontrada
            print("A palavra foi encontrada na linha:", i)                                         #Imprime a linha 
            break                                                                                  #Para o looping.
    for line in file:
        # print(line)
        # print(len(line))
        index = line.find('<?xml version="1.0" encoding="UTF-8"?>')
        if index != -1:
            print("A palavra foi encontrada na linha:", index+1)




print("--------------------------------------- 10) Operators")

   # *********** Operators *********** 

result = 10 + 30 # => 40
result = 40 - 10 # => 30
result = 50 * 5  # => 250
result = 16 / 4  # => 4.0 (Float Division)
result = 16 // 4 # => 4 (Integer Division)
result = 25 % 2  # => 1
result = 5 ** 3  # => 125

print(result)
        



print("--------------------------------------- 10) Exceptions")

    # *********** Exceptions ***********
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("You can't divide by zero!")
finally:
    print("Finally finished!")
 
#Try catch básico - Forçando um error, executando a impreensão de uma variável que não existe
try:
  print(x)
except NameError as error:
  print("Error Identificado: ",error)
except:
  print("Something else went wrong")



print("--------------------------------------- 11) Exceptions com classes e métodos customizados")

    # ***********Exceptions com classes e métodos customizados ***********

class TesteRealizadoComSucesso(Exception):  #Classe para tratamento de erros
    pass                                    # o serviço do pass é para que o tratamento de erros seja ignorado

    # *********** Função exception_test ***********
def exception_test():                                                                                                   # criando uma função para tratamento de erros
    with open("c:/Users/alammartins/Desktop/py/LearningPython/teste.txt", "r+", encoding='utf8') as file:               # abrindo arquivo indicado no parâmetro
        try:                                                                                                            # tratamento de erros
            texto = file.read()                                                                                         # lendo o arquivo
            texto += "\nInformação de teste realizado com sucesso"                                                      # adicionando uma nova linha
            file.seek(20)                                                                                               # posicionando o cursor
            file.write(texto)                                                                                           # escrevendo o arquivo
            file.truncate()                                                                                             # truncando o arquivo
        except Exception as e:                                                                                          # tratamento de erros
            raise TesteRealizadoComSucesso("Erro ao realizar teste na function exception_test: " + str(e)) from e       # tratamento de erros



    # *********** Função capturandoValorBkp ***********
def capturandoValorBkp():
    with open("c:/Users/alammartins/Desktop/py/LearningPython/bkp.txt", "r", encoding='utf8') as fileBkp: 
        
        # Iterando sobre o arquivo e procurando a existência da palavra "formAcompanhamentoPedidos" no arquivo.
        count = 0
        for line in fileBkp: #Lopping 
            count += 1
            index = line.find('formAcompanhamentoPedidos')  #Executando o recurso find que verifica se a palavra foi encontrada
            # print(index)
            if index != -1:     #Validando se a palavra foi encontrada (o recurso index retorna -1 se a palavra não for encontrada então caso ela for encontrada será retornado o valor do index)
                print("A palavra foi Identificada no arquivo. Linha:",count)
                print("Dados da linha: ",line)
 

try:                                            # tratamento de erros
    capturandoValorBkp()                        # chamando a função de tratamento de erros
    exception_test()                            # chamando a função de tratamento de erros
except TesteRealizadoComSucesso as e:           # Tratamento conforme a classe "TesteRealizadoComSucesso" que realiza a validação de tratamento, caso não tenha erro é retornado um pass para o proximo tratamento.
    print(e)                                    # Imprime o error
else:                                           # caso não seja ocorrido nenhum erro                                
    print("Teste realizado com sucesso")        # caso não seja ocorrido nenhum erro imprime esta mensagem de teste realizado com sucesso



print("--------------------------------------- ) ")