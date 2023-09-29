#Escreva um algoritmo para ler o #número total de eleitores de um
#município, o número de votos brancos, #nulos e válidos. Calcular e escrever o
#percentual que cada um representa em #relação ao total de eleitores

Eleitores = 0
VotosB = 0
Nulos = 0
validos = 0
percentualValidos = 0
percentualVotosB = 0
percentualNulos = 0

validos = float(input("informe o numero de Eleitores Validos: "))
VotosB = float(input("quantidades de votos brancos: "))
Nulos = float(input("votos Nulos: "))

Eleitores = validos+VotosB+Nulos

percentualValidos = (validos/Eleitores)*100
percentualVotosB = (VotosB/Eleitores)*100
percentualNulos = (Nulos/Eleitores)*100

print(f"\n o percentual de votos Válidos foi de {percentualValidos} % \n"
      f"o percentual de votos Nulos foi de {percentualNulos} % \n" 
      f"o percentual de votos Brancos foi de {percentualVotosB} % \n")
