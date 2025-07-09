#Estrtura de repetição com while 

numero = 1

while numero <=3:
    print(numero)
    numero+=1



#Validador de senha

senha = input('Digite sua senha: ')
while senha != "123":
    print("Senha errada")
    senha = input("Digite denovo ")
print ("Senha correta")


#Contar de cinco a um

numero = 5

while numero  <=1:
    print(numero)
    numero -=1
print('Finalizado')

#Mostara o menu até a pessoa digitar menu

menu = input('Digite sair')

while menu != "sair":
    print('Opção errada')
    menu = input('Digite novamente')
print ('Sair')

