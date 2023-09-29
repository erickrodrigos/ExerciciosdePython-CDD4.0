Entrada_Hora1 = 0
Entrada_Min1 = 0
Entrada_Hora2 = 0
Entrada_Min2 = 0


Entrada_Hora1 = int(input("insira a hora 1: "))
Entrada_Min1 = int(input("insira a minutos: "))
Entrada_Hora2 = int(input("insira a hora 2: "))
Entrada_Min2 = int(input("insira a minutos: "))

#caso uma variável esteja fora do horario Am/Pm transforma-la
if(Entrada_Hora1  >= 12 ):
   Entrada_Hora1  = Entrada_Hora1  - 12
if (Entrada_Hora2 >= 12):
    Entrada_Hora2 = Entrada_Hora2 - 12

SomaH = Entrada_Hora1 +Entrada_Hora2
if (SomaH >= 12):
    SomaH = SomaH -12
SomaM = Entrada_Min1 + Entrada_Min2
if(SomaM >= 60, SomaM <120):
    Hr = 1
    Min = SomaM - 60
    if(Min <0):
        Min = -1*Min

SomaH = (SomaH+Hr)
print(SomaH,":",Min)
