# Pedir o nome de tres pessoas, guardar em uma lista e dar boas vindas a cada um

#Forma um repetindo a solicitação
listName = []
listName.append(input('Digite um nome: '))
listName.append(input('Digite um nome: '))
listName.append(input('Digite um nome: '))
print(listName)


for i in listName:
    print(f'OBoa noite {i}')


#Forma dois usando o for para evitar redundância
listName = []
for i in range (3):
    listName.append(input('Digite um nome '))
    print(listName)

for i in listName:
    print(f'Boa noite {i}')
