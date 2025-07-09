#
cliente = {"nome": "Maria", "telefone": 11123456789, "cpf": "12345678-9", "endereço": "Rua Tito"}
print(cliente)
print(cliente["nome"])
print(cliente["telefone"])
print(cliente["cpf"])
print(cliente["endereço"])

print(len(cliente))

del cliente["nome"] #deletando item []
print(cliente)

cliente["nome"] = "Larissa" #atribuindo valor em item especifico []
print(cliente)

