#calcular o ano de nascimento da pessoa
repet = 1
while repet ==1:
    Idade = 0
    IdadeMes = 0
    Ano = 0
    MesAtual = 0
    AnoAtual = 0

    Idade = int(input("Informe a sua Idade: "))
    IdadeMes = int(input("Informe o numero do mes de nascimento:  "))
    MesAtual = int(input("Informe o numero do mes Atual:  "))
    AnoAtual = int(input("Informe o numero do Ano Atual:  "))

    Ano = AnoAtual-Idade

    if IdadeMes > MesAtual:
        Ano = Ano - 1
    print("o ano de nascimento foi : ", Ano)
    repet = int(input("Deseja realizar um novo calculo - Digite 1 : "))
