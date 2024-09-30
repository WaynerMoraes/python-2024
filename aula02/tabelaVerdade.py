#%%

idade = int(input("Digite sua idade: "))
cnh = input("Você tem CNH? ")

if idade >= 18 and cnh == "sim":
    print("Siga em frente")
else:
    print("Preso em nome da lei!")


#%%
#Tabela verdade com E
#OBS: Quando a tabela verdade e com a condição E, estamos multiplicando
print(bool(True * True))
print(bool(False * True))
print(bool(True * False))
print(bool(False * False))


#%%
#Tabela verdade com OU
#Quando a tabela verdade é com a condição OU, estamos somando
print(bool(True + True))
print(bool(False + True))
print(bool(True + False))
print(bool(False + False))