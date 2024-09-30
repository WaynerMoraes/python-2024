#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago


escolhaTipoSorvere = int(input("Escolha o tipo de sorvere: \n\n1-casquinha (R$1,00) \n2-cascão (R$2,50) \n3-cestinha (R$4,00) \n"))
valorTipoSorvete = float(0)

if escolhaTipoSorvere == 1:
    valorTipoSorvete = 1.00
    tipoSorvere = "Casquinha"
elif escolhaTipoSorvere == 2:
    valorTipoSorvete = 2.50
    tipoSorvere = "Cascão"
elif escolhaTipoSorvere == 3:
    valorTipoSorvete = 4.00
    tipoSorvere = "Cestinha"
else: 
    print("Opção inválida")


saborSorvete = int(input("\nEscolha o sabor do sorvere: \n\n1-morango \n2-creme \n3-chocolate\n"))

if saborSorvete == 1:
    saborSorvete = "morango"
elif saborSorvete == 2:
    saborSorvete = "creme"
elif saborSorvete == 3:
    saborSorvete = "chocolate"
else:
    print("Opção inválida")



escolhaSaborCobertura = int(input("\nEscolha o sabor do sorvere: \n1-Caramelo (R$1,50) \n2-morango (R$1,50) \n3-chocolate (R$1,50) \n4-sem cobertura (R$0,00)\n"))
valorCobertura = float(1.5)

if escolhaSaborCobertura == 1:
    saborCobertura = "Caramelo"
elif escolhaSaborCobertura == 2:
    saborCobertura = "Morango"
elif escolhaSaborCobertura == 3:
    saborCobertura = "Chocolate"
elif escolhaSaborCobertura == 4:
    saborCobertura = "Sem cobertura"
    valorCobertura = 0
else:
    print("Opção inválida")


print("O tipo de sorvete escolhido foi ", tipoSorvere, ", que custa R$",round(valorTipoSorvete,3))
print("O sabor do sorvete é ", saborSorvete)
print("A cobertura escolhida foi ", saborCobertura, ", que custa R$",round(valorCobertura,3))
print("O valor total ficou: R$",round(valorCobertura + valorTipoSorvete,3))