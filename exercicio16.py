"""Escreva um algoritmo para ler a hora de início e a hora de fim de um jogo
de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a
duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo
é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia
seguinte"""

HoraInicio = 0
HoraTermino = 0
TurnoInicio = 0
TurnoFinal = 0
Tempo = 0
Dia = 0

TurnoInicio = int(input("Indique em qual hora TURNO a partida se INICIOU a partida:\n 1 - MANHÃ \n 2 - TARDE/NOITE \n indique: "))

while TurnoInicio > 2 or TurnoInicio < 1:
    TurnoInicio = int(input("      AFIRMAÇÃO INCORRETA !!! \n "
    "Indique em qual hora TURNO a partida se INICIOU a partida:"
     "\n 1 - MANHÃ \n 2 - TARDE/NOITE \n indique: "))

HoraInicio = int(input("Indique em qual hora INICIOU a partida: "))

TurnoFinal = int(input("Indique em qual hora TURNO a partida TERMINOU a partida:\n 1 - MANHÃ \n 2 - TARDE/NOITE \n indique: "))

while TurnoFinal > 3 or TurnoInicio < 1:
    TurnoFinal = int(input("      AFIRMAÇÃO INCORRETA !!! \n "
    "Indique em qual hora TURNO a partida TERMINOU a partida:\n"
     "\n 1 - MANHÃ \n 2 - TARDE/NOITE \n indique: "))

HoraTermino = int(input("Indique em qual hora TERMINOU a partida: "))

if TurnoInicio == 2 and HoraInicio < 12:
    HoraInicio += 12

if TurnoFinal == 2 and HoraTermino < 12:
    HoraTermino += 12

Tempo = (HoraTermino - HoraInicio)
if Tempo < 0:
    Tempo = Tempo*(-1)
if (TurnoInicio == 1 and TurnoFinal == 1) or (TurnoInicio == 2 and TurnoFinal == 2):
    Tempo += 24
"""if Tempo > 24:
    Tempo -= 24
    Dia += 1"""

print("iNICIO ",HoraInicio)
print("TERMINO ",HoraTermino)
print(f" \n o tempo gasto na partida foi de {Tempo} Horas ")

