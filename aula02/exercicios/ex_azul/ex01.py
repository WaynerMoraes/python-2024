#%%

escolha = input("Você deseja uma água mineral ou com gás? ")


if escolha == "gas":
    qtd = int(input("Quantas você deseja? "))
    print("Você pediu ", qtd ,"águas com gás", "o valor total é de ", qtd * 2.50)
elif escolha == "mineral":
    qtd = int(input("Quantas você deseja? "))
    print("Você pediu ", qtd ,"águas minerais", "o valor total é de ", qtd * 1.50)
else:
    print("opção incorreta")

    