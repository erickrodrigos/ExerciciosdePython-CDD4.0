"""Escreva um algoritmo para ler a hora de início e a hora de fim de um jogo
de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a
duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo
é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia
seguinte"""

HoraInicio = 0
HoraTermino = 0
Tempo = 0

HoraInicio = int(input('Digite a hora do INICIO do jogo: '))
HoraTermino = int(input('Digite a hora do TERMINO do jogo: '))

Tempo = HoraTermino - HoraInicio

if Tempo < HoraInicio:
    resto = 24 - HoraInicio
    Tempo = HoraTermino + resto

print(f"O TEMPO DE DURAÇÃO FOI DE {Tempo}")

