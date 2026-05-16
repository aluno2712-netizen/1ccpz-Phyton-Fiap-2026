salas = [
     [28, 31, 34, 33],
     [25, 27, 29, 28],
     [32, 35, 36, 34],
     [24, 26, 25, 27],
]
i=0
sala_maior = 0
for sala in salas:
    print(sala)
    cont = 0
    print(f"Sala: ", i + 1)


    #= ou + 33
    for temp in sala:
        if temp >= 33:
            cont +=1

    media = sum(sala) / len(sala)



    print(f"A média das salas foi: {media}")
    print(f"Registros críticos: {cont}")
    print()




