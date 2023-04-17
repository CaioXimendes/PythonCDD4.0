time_1 = input("Digite o nome do Time 01: \n")
time_2 = input("Digite o nome do Time 02: \n")
gols_time_1 = int(input(f"Digite o número de gols marcados pelo {time_1}\n"))
gols_time_2 = int(input(f"Digite o número de gols marcados pelo {time_2}\n"))
if gols_time_1 == gols_time_2:
    print(f"Empate entre os times {time_1} e {time_2}, placar de: {gols_time_1}x{gols_time_2}")
else:
    if gols_time_1 > gols_time_2:
        print(f"Time vencedor foi: {time_1}, placar de: {gols_time_1}x{gols_time_2}")
    else:
        print(f"Time vencedor foi: {time_2}, placar de: {gols_time_1}x{gols_time_2}")