import os
from time import sleep

def verificador():  # Verifica quantos primos existem no arquivo (quantidade de linhas).
    reader = 0
    with open(r'primes.txt') as f:
        for i in f:
            reader += 1
    f.close()
    return reader


def conversor(texto):  # Conversor de string em valor inteiro.
    numero = texto.split()
    return int(numero[0])


def primos():  # Busca o ultimo primo resgistrado.
    global end
    file = open('primes.txt', 'r+')
    for i in range(verificador()):
        end = int(file.readline())
    file.close()
    return end


def calculadora(n):
# Calculadora de primos de acordo com os primos do banco de dados já calculado,
# e anexa ao arquivo um primo por vez.
    file = open('primes.txt', 'r')
    teste = 0
    for i in range(verificador()):
        numero = file.readline()
        primo = conversor(numero)
        if n % primo == 0:
            break
        else:
            teste += 1
    if teste == verificador():
        file = open('primes.txt', 'a')
        file.seek(2)
        file.write('\n' + str(n))
    file.close()


def progress_bar(done):
    print("\rProgress: [{0:50s}] {1:.3f}%".format('#' * int(done * 50), done * 100), end='')


def isfileexist():
    if os.path.isfile('primes.txt') == False:
        a = input("The file for the query does not exist, do you want continue?")
        if a.lower() in ['', 'n', 'not']:
            return False
        else:
            file = open("primes.txt", "w")
            file.write('2')
            file.close()
            print("The file was created to store the primes.")
            sleep(2)
            return True
    else:
        print("Primes Numbers: ", verificador())
        print("Last Prime Calculed: ", primos())
        action = input("Do you want to continue: ")
        if action.lower() in ['', 'n', 'not']:
            return False
        else:
            return True

Tasker = isfileexist()



while Tasker:
    try:
        i = primos()
        conta = 0
        numero = int(input("How much prime numbers would you like? "))
        if numero<verificador():
            print("The prime numbers was calculation yet.")
            break
        while (verificador() <= numero - 1):
            i += 1
            calculadora(i)
            progress_bar(verificador() / numero)
        input("\nAll the prime numbers was calculation.")
    except KeyboardInterrupt:
        answer= input("Do you want to stop the task?[Y/N]  ")
        if answer.lower() in ['y','sim','s','yes']:
            input("Task canceled!")
            exit()
        else:
            continue
    break
    if verificador() == numero - 1:
        input("\nAll the prime numbers was calculation.")
        break
if Tasker == False:
    input("Task canceled")
