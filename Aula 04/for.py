#Mostrar os numeros de um a cinco

for i in range (1,6):
    print(i)


#Dizer olá a uma lista de nomes

nomes = ["Maju", "Flora", "Penny"]

for i in nomes:
    print(f'Olá [i]')

#Numero maior que cem

numero = int(input('Digite um numero: '))

while numero <= 100:
    print('Tente noivamente ')
    numero = int(input())

print('Esse numero é maior que 100')

