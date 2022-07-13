#Al:Tupla com 20 primeiros colocados
# A mostrar os 5 primeiros, B os 4 ultimos, C) todos em ordem alfabética, D) em que posição está santos
#autor: Lucas Borguezam
#data:

#Import

#Inicio
times = ("Palmeiras", "Corinthians", "São Paulo", "Internacional", "Athletico-PR", "Atlético-MG", "Coritiba",
         "Fluminense", "América-MG", "Santos", "Bragantino", "Ceará", "Goiás", "Atlético-GO", "Flamengo", "Botafogo",
         "Cuiabá", "Avaí", "Juventude", "Fortaleza")

print("Top 5 do Brasileirão 2022/06")
print(times[:6])
print("-"*25);print("ultimos colocados")
print(times[-4:])
print("-" * 25);print("Ordem alfabética:")
print(sorted(times))
print("-" * 25)
print(f"Santos esta na {times.index('Santos') + 1}° posição")
#fim
